from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, username, password):
        """Create a new user"""
        if not email:
            raise ValueError("User must have an email address")
        if not username:
            raise ValueError("User must have a username")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, username, password):
        """Create a new superuser"""
        user = self.create_user(
            email = self.normalize_email(email), 
            username = username, 
            password = password,)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    objects = UserProfileManager()

    def get_full_username(self):
        """Retrieve full username of user"""
        return self.username

    def get_short_username(self):
        """Retrieve short username of user"""
        return self.username

    def __str__(self):
        """Return string representation of our user"""
        return self.email
