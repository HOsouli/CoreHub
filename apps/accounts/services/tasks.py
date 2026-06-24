from .sms_service import send_activation_sms
from celery import shared_task

@shared_task
def send_otp_sms_task(phone_number, code):
    print(f"--- [Celery] Starting to send sms to {phone_number} ---")

    success = send_activation_sms(phone_number, code)

    if success:
        print(f"--- [Celery] SMS successfully sent to {phone_number} ---")
        return f"SMS Send to {phone_number}"
    print(f"--- [Celery] Failed to send SMS to {phone_number} ---")
    return f"Failed to send SMS to {phone_number}"

