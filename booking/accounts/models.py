# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from phone_field import PhoneField
# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_save


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True,on_delete=models.CASCADE,default=True,related_name='profile')
	GENRE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('T','Transgender'),
    )
	firstname = models.CharField(max_length=100, blank=True)
	lastname = models.CharField(max_length=100, blank=True)
	mobile = PhoneField(blank=True)
	sex =  models.CharField(max_length=10, choices=GENRE_CHOICES, null=True)

	def __str__(self):
		return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)



