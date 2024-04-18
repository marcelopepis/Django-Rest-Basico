import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model where email is the unique identifiers
    for authentication instead of usernames.

    Args:
        AbstractBaseUser (): AbstractBaseUser class
        PermissionsMixin (): PermissionsMixin class
    """
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    first_name = models.CharField(verbose_name=_("first name"),
                                max_length=50)
    last_name = models.CharField(verbose_name=_("last name"),
                                max_length=50)
    email = models.EmailField(verbose_name=_("email address"),
                            db_index=True,
                            unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
    def __str__(self):
        # pylint: disable=E0307
        return self.first_name

    @property
    def get_full_name(self):
        # pylint: disable=E1101
        return f"{self.first_name.title()} {self.last_name.title()}"

    @property
    def get_short_name(self):
        # pylint: disable=E1101
        return self.first_name.title()
