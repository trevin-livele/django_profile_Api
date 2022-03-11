from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """manager for user profiles"""

    def create_user(self, email, username, password=None):
        """create a new user profile"""
        if not email:
            raise ValueError('user must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, username=username)


        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,  email, username, password):
        user = self.create_user(
            email  = self.normalize_email(email),
            username = username,
            password = password,
            
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        """retrieve full name of user"""
        return self.username

    def get_short_name(self):
        """Retrieve shot name of user"""
        return self.username

    def __str__(self):
        """return string representation of user"""
        return self.email