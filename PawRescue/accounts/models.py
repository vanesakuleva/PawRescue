from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, Permission, Group
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email!')
        if not username:
            raise ValueError('Users must have username!')

        user = self.model(
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)




class Account(AbstractBaseUser):
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

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    # from django.contrib.auth.base_user import BaseUserManager
    # from django.contrib.auth.hashers import make_password
    # from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, Permission, Group
    # from django.db import models
    #
    #
    #
    #
    # class CustomUserHandler(BaseUserManager):
    #
    #     def _create_user(self, email, password, **extra_fields):
    #         if not email:
    #             raise ValueError("The given username must be set")
    #
    #         user = self.model(email=email, **extra_fields)
    #         user.password = make_password(password)
    #         user.save(using=self._db)
    #         return user
    #
    #     def create_user(self, email, password=None, **extra_fields):
    #         if not email:
    #             raise ValueError('You must set a value for the Username field.')
    #
    #         extra_fields.setdefault("is_staff", False)
    #         extra_fields.setdefault("is_superuser", False)
    #         return self._create_user(email, password, **extra_fields)
    #
        def create_superuser(self, email, password=None, **extra_fields):
            extra_fields.setdefault('is_staff', True)
            extra_fields.setdefault('is_superuser', True)
    #
    #         if extra_fields.get('is_staff') is not True:
    #             raise ValueError('The superuser account requires the is_staff attribute to be set to True.')
    #         if extra_fields.get('is_superuser') is not True:
    #             raise ValueError('The superuser account requires the is_superuser attribute to be set to True.')
    #
    #         return self._create_user(email, password, **extra_fields)
    #
    #
    # class CustomUser(PermissionsMixin, AbstractBaseUser):
    #     email = models.EmailField(
    #         null=False,
    #         blank=False,
    #         unique=True,
    #     )
    #
    # is_active = models.BooleanField(
    #     default=True,
    # )
    #
    # is_staff = models.BooleanField(
    #     default=False,
    # )
    #
    # is_superuser = models.BooleanField(
    #     default=False
    # )

    # USERNAME_FIELD = 'email'
    #
    # REQUIRED_FIELDS = []
#
#     objects = CustomUserHandler()
#
#     class Meta:
#         default_related_name = 'accounts_custom_users'
#
# def __str__(self):
#     return self.email

#
# class Profile(models.Model):
#     first_name = models.CharField(
#         max_length=30,
#         null=False,
#         blank=False,
#     )
#     last_name = models.CharField(
#         max_length=30,
#         null=False,
#         blank=False,
#     )
#
#     email = models.EmailField(
#         unique=True,
#     )
#     age = models.PositiveIntegerField(
#         blank=False,
#         null=False,
#     )
#
#     # gender = models.CharField(
#     #     choices=Gender.choices(),
#     #     max_length=Gender.max_length(),
#     #
#     # )
#     # profileimage = models.URLField(
#     #     blank=True,
#     #     null=False,
#     # )
#     profile = models.OneToOneField(
#         CustomUser,
#         on_delete=models.CASCADE,
#         related_name='profile',
#     )
#     def get_full_name(self):
#         return f"{self.first_name} {self.last_name}"
#
#
