from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic= models.ImageField(null=True, blank=True, upload_to="images/profile/")
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    pinterest_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.user.first_name)



    def get_absolute_url(self):
        return reverse('profile', kwargs={'username': self.user.username})

    # def get_absolute_url(self):
    #     return reverse('profile', kwargs={'pk': self.pk})

    @property
    def profile(self):
        return self.user




    class Meta:
        verbose_name_plural = "User Profile"
