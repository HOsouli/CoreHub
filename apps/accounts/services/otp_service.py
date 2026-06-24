from apps.accounts.models import CustomUser
from .generator import generate_otp
from .jwt_service import get_token_for_user
from apps.accounts.models import OTP
from django.utils import timezone
from datetime import timedelta
from django.db import transaction
from rest_framework.exceptions import ValidationError
from apps.accounts.validate import mobile_validate
from apps.accounts.services.tasks import send_otp_sms_task

# _______________________________________________________________________
OTP_COOLDOWN = 120  # secounds allowed interval between two OTP code requests

def create_otp(phone_number):
    with transaction.atomic(): # Start secure transaction (nothing happens if operational storage fails)
        phone_number = mobile_validate(phone_number)

        now = timezone.now()
        last_otp = OTP.objects.filter(phone_number=phone_number).order_by("-created_at").first()

        # check previous OTP request
        if last_otp:
            seconds_passed = (now - last_otp.created_at).total_seconds()

            # Enforce request timeout
            if seconds_passed < OTP_COOLDOWN:
                remaining_time = int(OTP_COOLDOWN - seconds_passed)
                raise ValidationError(f"لطفا {remaining_time} ثانیه دیگر صبر کنید برای درخواست کد جدید")

        OTP.objects.filter(phone_number=phone_number).delete()  # Delete previous OTPs
        otp = OTP.objects.create(phone_number=phone_number, code=generate_otp(), expires_at=now + timedelta(minutes=5))

        transaction.on_commit(lambda: send_otp_sms_task.delay(phone_number, otp.code)) # Ensure task runs only after DB transaction is successfully saved
        return otp

# _______________________________________________________________________
MAX_ATTEMPTS = 5
BLOCKED_DURATION = timedelta(minutes=10)

def verify_otp(phone_number, code):
    with transaction.atomic():  # ensure DB consistency
        otp = OTP.objects.select_for_update().filter(phone_number=phone_number).order_by("-created_at").first()
        now = timezone.now()

        # OTP not found
        if not otp:
            raise ValidationError({"detail": "کد OTP پیدا نشد."})

        # user is blocked
        if otp.blocked_until and otp.blocked_until > now:
            remaining_seconds = int((otp.blocked_until - now).total_seconds())
            raise ValidationError({"detail": f"حساب شما تا {remaining_seconds} ثانیه دیگر مسدود است."})

        # OTP invalid (used or expired)
        if otp.is_used or otp.expires_at <= now:
            raise ValidationError({"detail": "کد OTP منقضی شده یا قبلاً استفاده شده است."})

        # wrong OTP
        if otp.code != code:
            otp.attempts += 1

            # too many attempts
            if otp.attempts >= MAX_ATTEMPTS:
                otp.blocked_until = now + BLOCKED_DURATION

            otp.save(update_fields=["attempts", "blocked_until"])

            raise ValidationError({"detail": "کد وارد شده صحیح نیست."})

        otp.is_used = True
        otp.attempts = 0
        otp.blocked_until = None
        otp.save(update_fields=["is_used", "attempts", "blocked_until"])

        user, created = CustomUser.objects.get_or_create(phone_number=phone_number)
        tokens = get_token_for_user(user)

        return {
            "user": user,
            "created": created,
            "tokens": tokens
        }

# _______________________________________________________________________
# -------Remember-------
# View is not going to create an OTP.
# View just gives commands.

# View → دستور
# Service → اجرا
