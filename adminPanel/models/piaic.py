from django.db import models
import django.utils.timezone
from ckeditor.fields import RichTextField


class PIAIC(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    heading = models.CharField(max_length=255, default="")
    tags = models.CharField(max_length=255, default="")
    instructions = models.CharField(max_length=255, default="")
    instructions_By = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())


class PIAIC_ICONS(models.Model):
    def upload_design_to(self, filename):
        return f'PIAICAttachments/Attachment_ID/ICONS{self.Icon_ID_id}/{filename}'

    Icon_ID = models.ForeignKey(PIAIC, on_delete=models.CASCADE)
    icons = models.FileField(upload_to=upload_design_to)


class PIAIC_Attachments(models.Model):
    def upload_design_to(self, filename):
        return f'PIAICAttachments/Attachment_ID/{self.Attachment_ID_id}/{filename}'

    Attachment_ID = models.ForeignKey(PIAIC, on_delete=models.CASCADE)
    files = models.FileField(upload_to=upload_design_to)


class PIAIC_Notifications(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default="")
    heading = models.CharField(max_length=255, default="")
    tags = models.CharField(max_length=255, default="")
    instructions = models.CharField(max_length=255, default="")
    instructions_By = models.CharField(max_length=255, default="")
    description = RichTextField(default="")
    image = models.FileField(upload_to='PIAICAttachments/Notification', default="")
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