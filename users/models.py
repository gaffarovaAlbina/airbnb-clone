from uuid import uuid4
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.utils.html import strip_tags
from django.template.loader import render_to_string


class User(AbstractUser):

    """Кастомная модель пользователя"""

    REQUIRED_FIELDS = ()

    GENDER_MALE = "мужчина"
    GENDER_FEMALE = "женщина"
    GENDER_OTHER = "другое"

    GENDER_CHOICES = (
        (GENDER_MALE, "мужчина"),
        (GENDER_FEMALE, "женщина"),
        (GENDER_OTHER, "другое"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_RISSIAN = "ru"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_RISSIAN, "Русский"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_RUB = "rub"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "Доллар США"),
        (CURRENCY_RUB, "Российский рубль"),
    )

    avatar = models.ImageField(null=True, blank=True, upload_to="avatars")
    gender = models.CharField(
        choices=GENDER_CHOICES, max_length=10, null=True, blank=True
    )
    bio = models.TextField(null=True, blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES,
        max_length=2,
        null=True,
        blank=True,
        default=LANGUAGE_RISSIAN,
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES,
        null=True,
        blank=True,
        max_length=3,
        default=CURRENCY_USD,
    )
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", context={"secret": secret}
            )
            send_mail(
                "Подтверждение аккаунта Airbnb",
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=True,
                html_message=html_message,
            )
            self.save()
        return
