import os

from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, Permission, Group, AbstractUser
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email or not username:
            raise ValueError('Users must have an email and username!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=35,
        verbose_name='email',
        null=False,
        blank=False,
        unique=True,
    )
    username = models.CharField(
        max_length=35,
        unique=True
    )

    date_joined = models.DateTimeField(
        verbose_name='date joined',
        auto_now_add=True,
    )

    last_log = models.DateTimeField(
        verbose_name='last login',
        auto_now=True,
    )

    is_admin = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_superuser = models.BooleanField(
        default=False
    )
    objects = AccountManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            Profile.objects.create(user=self)

    class Meta:
        default_related_name = 'accounts_custom_users'

    def __str__(self):
        return self.email


class Profile(models.Model):
    first_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default="",
    )
    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        default="",
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'{self.id} {self.get_full_name()}'

