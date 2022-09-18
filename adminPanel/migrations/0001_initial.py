# Generated by Django 4.1.1 on 2022-09-07 17:29

import ckeditor.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(default='', max_length=100)),
                ('Designation', models.CharField(default='', max_length=100)),
                ('street', models.CharField(default='', max_length=100)),
                ('areaofResearch', models.CharField(default='', max_length=100)),
                ('previousJob', models.CharField(default='', max_length=100)),
                ('School', models.CharField(default='', max_length=100)),
                ('Birthday', models.CharField(default='', max_length=100)),
                ('meritalStatus', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='', max_length=100)),
                ('Nationality', models.CharField(default='', max_length=100)),
                ('Skype', models.CharField(default='', max_length=100)),
                ('Phone', models.CharField(max_length=100, unique=True)),
                ('Email', models.EmailField(default='', max_length=254)),
                ('description', models.TextField(default='')),
                ('resume', models.FileField(default='', upload_to='Resume')),
                ('profile', models.ImageField(default='', upload_to='profiles')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('School', models.CharField(default='', max_length=100)),
                ('StudyArea', models.CharField(default='', max_length=100)),
                ('From', models.CharField(default='', max_length=100)),
                ('To', models.CharField(default='', max_length=100)),
                ('Icon', models.ImageField(default='', upload_to='Education')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(default='', max_length=100)),
                ('From', models.CharField(default='', max_length=100)),
                ('To', models.CharField(default='', max_length=100)),
                ('Company', models.CharField(default='', max_length=100)),
                ('Street', models.CharField(default='', max_length=100)),
                ('Description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='hello',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yourName', models.CharField(default='', max_length=100)),
                ('email', models.EmailField(default='', max_length=254)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='LangSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill1', models.CharField(default='', max_length=100)),
                ('expert1', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('skill2', models.CharField(default='', max_length=100)),
                ('expert2', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('skill3', models.CharField(default='', max_length=100)),
                ('expert3', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('skill4', models.CharField(default='', max_length=100)),
                ('expert4', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('skill5', models.CharField(default='', max_length=100)),
                ('expert5', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('skill6', models.CharField(default='', max_length=100)),
                ('expert6', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('skill7', models.CharField(default='', max_length=100)),
                ('expert7', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('skill8', models.CharField(default='', max_length=100)),
                ('expert8', models.CharField(choices=[('10%', '10%'), ('30%', '30%'), ('50%', '50%'), ('70%', '70%'), ('90%', '90%'), ('100%', '100%')], default='', max_length=100)),
                ('lang1', models.CharField(default='', max_length=100)),
                ('str1', models.CharField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='', max_length=100)),
                ('lang2', models.CharField(default='', max_length=100)),
                ('str2', models.CharField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='', max_length=100)),
                ('lang3', models.CharField(default='', max_length=100)),
                ('str3', models.CharField(choices=[('Basic', 'Basic'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='', max_length=100)),
                ('Icon1', models.ImageField(default='', upload_to='LangSkill/langIcons')),
                ('Icon2', models.ImageField(default='', upload_to='LangSkill/langIcons')),
                ('Icon3', models.ImageField(default='', upload_to='LangSkill/langIcons')),
            ],
        ),
        migrations.CreateModel(
            name='Portfolios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(default='', max_length=300)),
                ('thumbnail', models.ImageField(default='', upload_to='Portfolio/Thumbnails')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.CharField(default='', max_length=100)),
                ('designation', models.CharField(default='', max_length=100)),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(default='', max_length=100)),
                ('skype', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=100)),
                ('github', models.CharField(default='', max_length=100)),
                ('linkedin', models.CharField(default='', max_length=100)),
                ('google_plus', models.CharField(default='', max_length=100)),
                ('youtube', models.CharField(default='', max_length=100)),
                ('website', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='userBlog',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('heading', models.CharField(default='', max_length=255)),
                ('tags', models.CharField(default='', max_length=255)),
                ('quote', models.CharField(default='', max_length=255)),
                ('quote_by', models.CharField(default='', max_length=255)),
                ('description', ckeditor.fields.RichTextField(default='')),
                ('Icon', models.ImageField(default='', upload_to='Blog/Icons')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 9, 7, 17, 29, 37, 325361, tzinfo=datetime.timezone.utc))),
            ],
        ),
        migrations.CreateModel(
            name='blog_Review',
            fields=[
                ('sNo', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('comment', models.TextField(default='')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminPanel.blog_review')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminPanel.userblog')),
            ],
        ),
    ]
