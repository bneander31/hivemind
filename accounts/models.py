from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    # User,
)
from django.core.validators import RegexValidator
from django.db import models
# from datetime import datetime
# from django import forms
from django.core.mail import send_mail
from django.db.models.signals import post_save
from .utils import code_generator

USERNAME_REGEX = '^[a-zA-Z0-9.@+-]*$'


class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=255,
                                validators=[
                                    RegexValidator(
                                        regex=USERNAME_REGEX,
                                        message='Username must be Alphanumeric or'
                                                ' contain any of the following: ". @ + -"',
                                        code='invalid_username'
                                    )],
                                unique=True,
                                )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=120, default='60406')
    tel = models.CharField(max_length=15, null='888-888-8888', blank='888-888-8888', default='888-888-8888')
    street_address = models.CharField(max_length=300, null='Street Address', blank='Street Address',
                                      default='Street Address')
    city = models.CharField(max_length=200, null='City', blank='City', default='City')
    state = models.CharField(max_length=200, null='State', blank='State', default='State')
    picture = models.ImageField(upload_to='photos/accounts/%Y/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=300, null=True, blank=True)
    tel = models.CharField(max_length=15, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(default='profile_img.jpg', upload_to='photos/accounts/%Y/')
    bio = models.TextField()

    def __str__(self):
        return str(self.user.username)


def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
            # ActivationProfile.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)
