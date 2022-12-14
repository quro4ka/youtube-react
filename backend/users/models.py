from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        return self._create_user(email, password, **extra_fields)
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'

    GENDERS = (
    ('m', "Мужчина"),
    ('f', "Женщина"))


    gender = models.CharField(choices=GENDERS, max_length=1, default='')
    birth_date = models.DateField(default="2000-09-12")
    image = models.ImageField(upload_to='image/user/logo/%Y/%m/', null=True)
    is_block = models.BooleanField(default=0)

    REQUIRED_FIELDS = []

    def get_email(self):
        return self.username

    objects = CustomUserManager()
