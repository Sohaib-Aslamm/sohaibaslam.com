from django.db import models
import django.utils.timezone
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class userBlog(models.Model):
    sNo = models.AutoField(primary_key=True)
    title = models.TextField(default="")
    slug = models.SlugField(max_length=200, unique=True, null=True, default=None)
    heading = models.TextField(default="")
    tags = models.TextField(default="")
    quote = models.TextField(default="")
    quote_by = models.TextField(default="")
    description = RichTextField(default="")
    Icon = models.FileField(upload_to='Blog/Icons', default="")
    created_at = models.DateTimeField(default=django.utils.timezone.now())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class blog_Review(models.Model):
    sNo = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200, default="")
    comment = models.TextField(default="")
    post = models.ForeignKey(userBlog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=django.utils.timezone.now)