from django.db import models


class Recommendations(models.Model):
    person = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=1000, default="")