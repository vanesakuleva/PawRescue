from django.db import models

from PawRescue.accounts.forms import User
from PawRescue.pets.models import Pet
from PawRescue.accounts.models import Account
from PawRescue.utilities.validators import validate_word_count


class AdoptionEvent(models.Model):
    MAX_LENGTH = 50
    MAX_LENGTH_HASHTAGS = 200
    name = models.CharField(
        max_length=MAX_LENGTH
    )

    description = models.TextField(
        validators=[validate_word_count],
        blank=False,
        null=False
    )

    location = models.CharField(
        max_length=MAX_LENGTH,
        blank=False,
        null=False
    )

    start_date = models.DateTimeField(

    )

    end_date = models.DateTimeField(

    )

    photo = models.ImageField(
        upload_to='event_photos/',
        blank=True,
        null=True

    )

    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    participant_count = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return self.name


class EventPet(models.Model):
    event = models.ForeignKey(
        AdoptionEvent,
        on_delete=models.CASCADE
    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.event} - {self.pet}"
