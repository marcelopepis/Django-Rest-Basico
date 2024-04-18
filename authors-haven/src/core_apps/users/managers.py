"""
file for custom user manager
"""
from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.

    Args:
        BaseUserManager (): BaseUserManager class
    """
    def email_validator(self, email):
        """Email validator

        Args:
            email (): email address

        Raises:
            ValueError: Enter a valid email address.

        Returns:
            type: bool
        """
        try:
            validate_email(email)
            return True
        except ValidationError as exc:
            raise ValueError(_('Enter a valid email address.')) from exc

    def create_user(self, first_name,last_name,email,password, **extra_fields):
        """Create and return a regular user with an email, first name, last name and password.

        Args:
            first_name (string): first name
            last_name (string): last name
            email (string): email address
            password (string): password

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: 

        Returns:
            _type_: _description_
        """
        if not first_name:
            raise ValueError(_('The First Name must be set'))
        if not last_name:
            raise ValueError(_('The Last Name must be set'))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('The Email must be set'))
        user = self.model(first_name=first_name,last_name=last_name,email=email, **extra_fields)
        user.set_password(password)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name,last_name,email,password, **extra_fields):
        """Create and return a superuser with an email, first name, last name and password.

        Args:
            first_name (string): first name
            last_name (string): last name
            email (string): email address
            password (string): password

        Raises:
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_
            ValueError: _description_

        Returns:
            _type_: _description_
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        if not password:
            raise ValueError(_('Superuser must have a password.'))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_('The Email must be set'))
        user = self.create_user(first_name=first_name,
                                last_name=last_name,
                                email=email, **extra_fields)
        user.save(using=self._db)
        return user
