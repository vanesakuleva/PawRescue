from django.db import models
from PawRescue.pets.models import Pet
from PawRescue.accounts.models import Account
from PawRescue.utilities.validators import validate_word_count, validate_digits_only


class Adoption(models.Model):
    MAX_LENGTH_CHOICES = 35
    MAX_LENGTH_NUMBER = 10
    STATUS_CHOICES = (
        ('Pending', 'Pending - Your Application is Under Review'),
        ('Accepted', 'Accepted - Expect a Call from the Pet Owner'),
        ('Rejected', 'Rejected - Thank You for Applying'),
    )

    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='adoptions'

    )

    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE
    )

    pet_owner = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name='owned_adoptions'
    )

    adoption_date = models.DateField(
        null=True,
        blank=True,
    )

    is_completed = models.BooleanField(
        default=False

    )

    contact_number = models.CharField(
        max_length=MAX_LENGTH_NUMBER,
        blank=False,
        null=False,
        validators=[validate_digits_only],
    )

    home_environment = models.TextField(
        validators=[validate_word_count],
        blank=False,
        null=False,
    )
    previous_pet_experience = models.TextField(
        validators=[validate_word_count],
        blank=False,
        null=False,
    )

    reason_for_adoption = models.TextField(
        validators=[validate_word_count],
        blank=False,
        null=False,
    )

    status = models.CharField(
        max_length=MAX_LENGTH_CHOICES,
        choices=STATUS_CHOICES,
        default='Pending'

    )

    def __str__(self):
        return f"{self.user.username} - {self.pet.name}"


class ApprovedAdoption(models.Model):
    adoption = models.ForeignKey(Adoption, on_delete=models.CASCADE)
    approval_date = models.DateTimeField(auto_now_add=True)
