# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-11 12:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('login', '0002_signup_album_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Department', models.CharField(default='', max_length=300)),
                ('Designation', models.CharField(default='', max_length=300)),
                ('Phone', models.IntegerField(default=0)),
                ('RoomNo', models.CharField(max_length=200)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_image')),
                ('Fax', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]