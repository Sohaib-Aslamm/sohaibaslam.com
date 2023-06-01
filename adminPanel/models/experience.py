from django.db import models


class Experience(models.Model):
    Designation = models.CharField(max_length=100, default="")
    From = models.CharField(max_length=100, default="")
    To = models.CharField(max_length=100, default="")
    Company = models.CharField(max_length=100, default="")
    Street = models.CharField(max_length=100, default="")