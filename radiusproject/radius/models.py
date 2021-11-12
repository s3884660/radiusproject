import uuid

import datetime as datetime
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class ActivityTags(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a Tag (e.g. Community')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=200, help_text='Activity Name')
    description = models.TextField(help_text='Activity Description')
    address = models.CharField(max_length=200, help_text='Activity Address')
    tags = models.ManyToManyField(ActivityTags, help_text='Select Tags')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Activity Key')
    datetime = models.DateTimeField(default=datetime.datetime.now())
    longitude = models.FloatField(default=151.7420)
    latitude = models.FloatField(default=-33.871846)
    image = models.ImageField(upload_to='images/', default='noimage.jpg')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

    def get_absolute_url(self):
        """Returns the url to access a detail record for this activity."""
        return reverse('activity-detail', args=[str(self.id)])


# Defined for possible use later but not currently used
class ActivityInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Instance ID')
    activity = models.ForeignKey('Activity', on_delete=models.RESTRICT, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.activity.name})'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interests = models.ManyToManyField(ActivityTags)
    bio = models.TextField(help_text='User Bio', blank=True)
    location = models.CharField(max_length=30, blank=True)
    AVATAR_CHOICES = [
        (1, 'avat1.png'),
        (2, 'avat2.png'),
        (3, 'avat3.png'),
        (4, 'avat4.png'),
        (5, 'avat5.png'),
        (6, 'avat6.png'),
        (7, 'avat7.png'),
    ]
    avatar = models.IntegerField(
        choices=AVATAR_CHOICES,
        default=1
    )

# Apparently putting the signals here is the ugly way to do it but this is getting frustrating
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()