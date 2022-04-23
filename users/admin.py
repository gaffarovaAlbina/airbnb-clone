from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Кастомная админка для пользователей"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                )
            },
        ),
    )
    list_display = (
        "username",
        "email",
        "gender",
        "language",
        "currency",
        "superhost",
        "email_verified",
        "email_secret",
    )
    list_filter = ()
