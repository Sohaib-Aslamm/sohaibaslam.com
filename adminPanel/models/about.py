from django.db import models


Merital_Status = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
)


class About(models.Model):
    fullName = models.CharField(max_length=100, default="")
    Designation = models.CharField(max_length=100, default="")
    street = models.CharField(max_length=100, default="")
    areaofResearch = models.CharField(max_length=100, default="")
    previousJob = models.CharField(max_length=100, default="")
    School = models.CharField(max_length=100, default="")
    Birthday = models.CharField(max_length=100, default="")
    meritalStatus = models.CharField(max_length=100, choices=Merital_Status, default="")
    Nationality = models.CharField(max_length=100, default="")
    Skype = models.CharField(max_length=100, default="")
    Phone = models.CharField(max_length=100, unique=True)
    Email = models.EmailField(default="")
    description = models.TextField(default="")
    resume = models.FileField(upload_to='Resume', default="")
    profile = models.FileField(upload_to='profiles', default="")