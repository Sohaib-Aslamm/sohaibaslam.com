from django.db import models


class SocialMedia(models.Model):
    sNo = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, default="")
    skype = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")
    github = models.CharField(max_length=100, default="")
    linkedin = models.CharField(max_length=100, default="")
    google_plus = models.CharField(max_length=100, default="")
    youtube = models.CharField(max_length=100, default="")
    website = models.CharField(max_length=100, default="")