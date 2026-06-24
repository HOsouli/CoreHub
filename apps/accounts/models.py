from django.db import models
from .validate import mobile_validate
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from utils import FileUpload
from django.utils import timezone


# It says "How to build management"
class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("شماره موبایل را وارد کنید")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)  # Permission to enter the admin panel with restricted access
        extra_fields.setdefault("is_superuser", True)  # Allow the admin panel to control the entire system
        extra_fields.setdefault("is_active", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be is_superuser=True")
        return self.create_user(phone_number, password, **extra_fields)


# It says "How to build a model"
class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=11, unique=True, validators=[mobile_validate], verbose_name="شماره موبایل")
    email = models.EmailField(blank=True, null=True, verbose_name="ایمیل")
    first_name = models.CharField(max_length=50, blank=True, verbose_name="نام")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="نام خانوادگی")
    is_active = models.BooleanField(default=True, verbose_name="فعال/غیرفعال")
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ عضویت")

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS: list = []

    def __str__(self):
        return f'{self.first_name} {self.last_name}'.strip() or self.phone_number

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True, related_name="customer")
    address = models.TextField(blank=True, verbose_name="آدرس")
    file_upload = FileUpload("image", "customer")
    image_name = models.ImageField(upload_to=file_upload.upload_to, blank=True, null=True, verbose_name="تصویر پروفایل")
    profile_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتریان'
        ordering = ['-created_at']


# ______________________________________________________________________
class OTP(models.Model):
    phone_number = models.CharField(max_length=11, validators=[mobile_validate], verbose_name="شماره موبایل")
    code = models.CharField(max_length=6, verbose_name="کد تایید")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    expires_at = models.DateTimeField(verbose_name="زمان انقضا")
    is_used = models.BooleanField(default=False, verbose_name="استفاده شده")
    attempts = models.PositiveSmallIntegerField(default=0, verbose_name="تعداد تلاش")
    blocked_until = models.DateTimeField(blank=True, null=True, verbose_name="زمان پایان مسدودسازی")

    def is_valid(self):
        if self.blocked_until and self.blocked_until > timezone.now(): # نامعتبر است OTP زمان پایان مسدودی هنوز از الان جلوتر است پس مونده تا پایان مسدودی بنابراین
            return False
        return not self.is_used and timezone.now() < self.expires_at

    def __str__(self):
        return f"{self.phone_number} - {self.code}"

    class Meta:
        verbose_name = "کد تایید (OTP)"
        verbose_name_plural = "کدهای تایید (OTP)"

