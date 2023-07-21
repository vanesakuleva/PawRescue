from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User

from PawRescue.accounts.models import Account
from PawRescue.utilities.validators import validate_word_count


class Pet(models.Model):
    DEFAULT_TYPE = 'Unknown'
    PET_TYPES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Other', 'Other')
    ]

    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Unknown', 'Unknown')
    ]

    HEALTH_STATUS_CHOICES = [
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Serious', 'Serious'),
        ('Critical', 'Critical')
    ]
    name = models.CharField(
        max_length=20,
        blank=True,
        default="To Be Named"

    )
    pet_type = models.CharField(
        max_length=10,
        choices=PET_TYPES

    )

    other_pet_type = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    breed = models.CharField(
        max_length=20,
        blank=True,
        default=DEFAULT_TYPE
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    gender = models.CharField(
        max_length=10,
        choices=GENDERS,
        default=DEFAULT_TYPE
    )

    description = models.TextField(
        validators=[validate_word_count]
    )

    specifics_in_behavior = models.TextField(
        validators=[validate_word_count]

    )
    health_status = models.CharField(
        max_length=10,
        choices=HEALTH_STATUS_CHOICES,
        default='Good'
    )

    photo = models.ImageField(
        upload_to='pet_photos/'
    )

    town = models.CharField(
        max_length=35
    )

    can_be_driven = models.BooleanField(
        default=False
    )

    created_by = models.ForeignKey(
        Account,
        on_delete=models.CASCADE

    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    @property
    def health_status_text(self):
        if self.health_status == 'Good':
            return "The pet is in good health."
        elif self.health_status == 'Fair':
            return "The pet has some health concerns but is generally doing well."
        elif self.health_status == 'Serious':
            return "The pet has significant health issues that require attention."
        elif self.health_status == 'Critical':
            return "The pet is in critical condition and needs immediate medical care."
        else:
            return "Health status information not available."
