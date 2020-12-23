from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        user = self.set_new_values_to_user(email, password, extra_fields)
        user.save(using=self._db)
        return user

    def set_new_values_to_user(self, email, password, extra_fields):
        if not email:
            raise ValueError("Email cannot be null")
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):
    """ Custom user model that supports using email instead of username """
    email =  models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD  = 'email'

