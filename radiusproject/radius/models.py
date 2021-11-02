import uuid

import datetime as datetime
from django.db import models
from django.urls import reverse


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
