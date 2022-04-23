from django.db import models
from core import models as core_models
from django.utils import timezone


class Reservation(core_models.TimeStampedModel):
    """Модель бронирований"""

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELED = "canceled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Ожидание подтверждения"),
        (STATUS_CONFIRMED, "Бронирование отменено"),
        (STATUS_CANCELED, "Бронирование подтверждено"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    guest = models.ForeignKey(
        "users.User", related_name="reservations", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reservations", on_delete=models.CASCADE
    )
    check_in = models.DateField()
    check_out = models.DateField()

    def in_progress(self):
        now = timezone.now().date()
        return now >= self.check_in and now <= self.check_out

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    in_progress.boolean = True
    is_finished.boolean = True
