from django.db import models


class Portfolios(models.Model):
    link = models.CharField(max_length=300, default="")
    thumbnail = models.FileField(upload_to='Portfolio/Thumbnails', default="")