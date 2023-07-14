from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, Permission, Group
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email!')
        if not username:
            raise ValueError('Users must have a username!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, ):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


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
    objects = AccountManager()
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    class Meta:
        default_related_name = 'accounts_custom_users'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self,
                         app_label):  # checks if the user has permissions to view the app with the given app_label
        return True


class Profile(models.Model):
    # DEFAULT_PROFILE_PICTURE = os.getenv('DEFAULT_PROFILE_PICTURE')
    first_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    last_name = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        blank=False,
        null=False,
    )
    profile_picture = models.URLField(
        # default=DEFAULT_PROFILE_PICTURE,
        blank=True,
        null=False,
    )

    user = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        related_name='profile',
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f'{self.id} {self.get_full_name()}'
