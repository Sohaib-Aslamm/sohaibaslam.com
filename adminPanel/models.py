from django.db import models
import django.utils.timezone
from ckeditor.fields import RichTextField

# Create your models here.


Merital_Status = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Divorced', 'Divorced'),
)

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
    profile = models.ImageField(upload_to='profiles', default="")


class Experience(models.Model):
    Designation = models.CharField(max_length=100, default="")
    From = models.CharField(max_length=100, default="")
    To = models.CharField(max_length=100, default="")
    Company = models.CharField(max_length=100, default="")
    Street = models.CharField(max_length=100, default="")
    Description = models.CharField(max_length=1000, default="")


class Education(models.Model):
    School = models.CharField(max_length=100, default="")
    StudyArea = models.CharField(max_length=100, default="")
    From = models.CharField(max_length=100, default="")
    To = models.CharField(max_length=100, default="")
    Icon = models.ImageField(upload_to='Education', default="")


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
    Icon1 = models.ImageField(upload_to='LangSkill/langIcons', default="")
    Icon2 = models.ImageField(upload_to='LangSkill/langIcons', default="")
    Icon3 = models.ImageField(upload_to='LangSkill/langIcons', default="")


class Portfolios(models.Model):
    link = models.CharField(max_length=300, default="")
    thumbnail = models.ImageField(upload_to='Portfolio/Thumbnails', default="")


class Recommendations(models.Model):
    person = models.CharField(max_length=100, default="")
    designation = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=1000, default="")



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


class userBlog(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    heading = models.CharField(max_length=255, default="")
    tags = models.CharField(max_length=255, default="")
    quote = models.CharField(max_length=255, default="")
    quote_by = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    Icon = models.ImageField(upload_to='Blog/Icons', default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())



class blog_Review(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    comment = models.TextField(default="")
    post = models.ForeignKey(userBlog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)



class hello(models.Model):
    yourName = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    description = models.TextField(default="")


class PIAIC(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    tags = models.CharField(max_length=255, default="")
    instructions = models.CharField(max_length=255, default="")
    instructions_By = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())


class PIAIC_Attachments(models.Model):
    def upload_design_to(self, filename):
        return f'PIAICAttachments/Attachment_ID/{self.Attachment_ID_id}/{filename}'

    Attachment_ID = models.ForeignKey(PIAIC, on_delete=models.CASCADE)
    files = models.FileField(upload_to=upload_design_to)



class PIAIC_Notifications(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    tags = models.CharField(max_length=255, default="")
    instructions = models.CharField(max_length=255, default="")
    instructions_By = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    image = models.ImageField(upload_to='PIAICAttachments/Notification', default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())



class PIAIC_Review(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    comment = models.TextField(default="")
    post = models.ForeignKey(PIAIC, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)



class PIAIC_NOTIFI_Review(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    comment = models.TextField(default="")
    post = models.ForeignKey(PIAIC_Notifications, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)