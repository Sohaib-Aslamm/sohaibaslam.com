from django.db import models


Expert_Skills = (
    ('10%', '10%'),
    ('30%', '30%'),
    ('50%', '50%'),
    ('70%', '70%'),
    ('90%', '90%'),
    ('100%', '100%'),
)

Expert_Lang = (
    ('Basic', 'Basic'),
    ('Intermediate', 'Intermediate'),
    ('Advanced', 'Advanced'),
)


class LangSkill(models.Model):
    skill1 = models.CharField(max_length=100, default="")
    expert1 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    skill2 = models.CharField(max_length=100, default="")
    expert2 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    skill3 = models.CharField(max_length=100, default="")
    expert3 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    skill4 = models.CharField(max_length=100, default="")
    expert4 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    skill5 = models.CharField(max_length=100, default="")
    expert5 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    skill6 = models.CharField(max_length=100, default="")
    expert6 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    skill7 = models.CharField(max_length=100, default="")
    expert7 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    skill8 = models.CharField(max_length=100, default="")
    expert8 = models.CharField(max_length=100, choices=Expert_Skills, default="")
    lang1 = models.CharField(max_length=100, default="")
    str1 = models.CharField(max_length=100, choices=Expert_Lang, default="")
    lang2 = models.CharField(max_length=100, default="")
    str2 = models.CharField(max_length=100, choices=Expert_Lang, default="")
    lang3 = models.CharField(max_length=100, default="")
    str3 = models.CharField(max_length=100, choices=Expert_Lang, default="")
    Icon1 = models.FileField(upload_to='LangSkill/langIcons', default="")
    Icon2 = models.FileField(upload_to='LangSkill/langIcons', default="")
    Icon3 = models.FileField(upload_to='LangSkill/langIcons', default="")