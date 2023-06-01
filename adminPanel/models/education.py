from django.db import models


class Education(models.Model):
    School = models.CharField(max_length=100, default="")
    StudyArea = models.CharField(max_length=100, default="")
    From = models.CharField(max_length=100, default="")
    To = models.CharField(max_length=100, default="")
    Icon = models.FileField(upload_to='Education', default="")