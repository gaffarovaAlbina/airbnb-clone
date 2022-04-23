from datetime import datetime, timedelta
import random
from django.core.management.base import BaseCommand, CommandError
from django.contrib.admin.utils import flatten
from django_seed import Seed
import reservations.models as reservation_models
import users.models as user_models
import rooms.models as room_models


class Command(BaseCommand):

    help = "Эта команда генерирует бронирования в базе данных"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            help="Сколько броинрований создать в базе данных",
        )

    def handle(self, *args, **options):
        number = int(options.get("number"))
        user = user_models.User.objects.all()
        room = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            reservation_models.Reservation,
            number,
            {
                "status": lambda x: random.choice(["pending", "confirmed", "canceled"]),
                "guest": lambda x: random.choice(user),
                "room": lambda x: random.choice(room),
                "check_in": lambda x: datetime.now(),
                "check_out": lambda x: datetime.now()
                + timedelta(days=random.randint(3, 25)),
            },
        )

        seeder.execute()

        self.stdout.write(self.style.SUCCESS(f"{number} бронирований создано!"))
