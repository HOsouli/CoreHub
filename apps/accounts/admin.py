from django.contrib import admin
from .models import CustomUser, Customer
from .models import OTP

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "email", "first_name", "last_name", "is_active", "is_staff", "date_joined")
    list_filter = ("is_active", "is_staff", "date_joined")
    search_fields = ("phone_number", "first_name", "last_name")
    ordering = ("-date_joined",)
    fieldsets = (
    (
        "اطلاعات کاربر",
        {
            "fields": (
                "phone_number",
                "email",
                "first_name",
                "last_name",
            )
        }
    ),

    (
        "سطح دسترسی",
        {
            "fields": (
                "is_active",
                "is_staff"
            )
        }
    ),
)
list_editable = ("is_active",)
list_per_page = 20


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("user", "profile_completed", "created_at", "updated_at")
    ordering = ("-created_at",)
    list_filter = ("created_at", "profile_completed")
    search_fields = ("user__phone_number", "user__first_name", "user__last_name")
    readonly_fields = ("created_at", "updated_at")
    autocomplete_fields = ("user",)
    list_per_page = 20
    fieldsets = (
        (
            "اطلاعات کاربر",
            {
                "fields": (
                    "user",
                    "profile_completed",
                )
            },
        ),

        (
            "پروفایل",
            {
                "fields": (
                    "address",
                    "image_name",
                )
            },
        ),

        (
            "زمان‌ها",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                )
            },
        ),
    )

    actions = ("mark_completed",)
    def mark_completed(self, request, queryset):
        updated = queryset.update(profile_completed=True)
        self.message_user(request, f"{updated} پروفایل تکمیل شد")

    mark_completed.short_description = "تکمیل کردن پروفایل انتخاب‌شده‌ها"



@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ("phone_number", "code", "created_at", "expires_at", "is_used")
    list_filter = ("is_used", "created_at")
    search_fields = ("phone_number", "code")
    readonly_fields = ("created_at",)
