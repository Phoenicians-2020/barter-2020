from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

optional = {
    'null': True,
    'blank': True
}


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), max_length=255, **optional)


class Interests(models.Model):
    name = models.CharField(max_length=150, **optional)
    date_created = models.DateField(default=timezone.now, **optional)
    date_updated = models.DateField(default=timezone.now, **optional)


class Profile(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile")
    about_me = models.CharField(max_length=155, **optional)
    profile_photo = models.ImageField(upload_to='profile_images/', **optional)
    address = models.CharField(max_length=225, **optional)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, **optional)
    interest = models.ManyToManyField(Interests, related_name="profile")

    def __str__(self):
        return self.user.name
