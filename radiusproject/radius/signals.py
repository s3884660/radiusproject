from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from models import ActivityTags


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


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()