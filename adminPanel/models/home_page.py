from django.db import models


class MainPage(models.Model):
    name = models.TextField(default="")
    skills = models.TextField(default="")
    tag_line = models.TextField(default="")
    description_1 = models.TextField(default="")
    description_2 = models.TextField(default="")
