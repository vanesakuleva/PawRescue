from django.db import models

from django.db import models

from PawRescue.utilities.validators import validate_digits_only, validate_word_count


class VolunteerApplication(models.Model):
    MAX_LENGTH = 35
    MAX_LENGTH_NUMBER = 10
    MAX_LENGTH_ADDRESS = 50
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )

    full_name = models.CharField(
        max_length=MAX_LENGTH
    )

    email = models.EmailField(
        max_length=MAX_LENGTH,
        verbose_name='email',
        null=False,
        blank=False,
    )

    contact_number = models.CharField(
        max_length=MAX_LENGTH_NUMBER,
        blank=False,
        null=False,
        validators=[validate_digits_only],
    )
    address = models.TextField(
        max_length=MAX_LENGTH_ADDRESS,
        blank=False,
        null=False,
    )
    skills = models.CharField(
        max_length=200,
        blank=True, null=True
    )

    availability = models.CharField(
        validators=[validate_word_count],
        blank=False,
        null=False,
    )

    why_volunteer = models.TextField(
        validators=[validate_word_count],
        blank=False,
        null=False,
    )

    applied_date = models.DateTimeField(
        auto_now_add=True
    )

    status = models.CharField(
        max_length=MAX_LENGTH,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    def __str__(self):
        return f"Volunteer Application #{self.id}"
