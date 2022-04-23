from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):
    """Модель диалогов"""

    participants = models.ManyToManyField(
        "users.User", related_name="conversations", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_messages(self):
        return self.messages.count()

    def count_participants(self):
        return self.participants.count()

    count_messages.short_description = "Number of messages"
    count_participants.short_description = "Number of participants"


class Message(core_models.TimeStampedModel):
    """Модель сообщений"""

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="conservations", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="conservations", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} написал: {self.message}"
