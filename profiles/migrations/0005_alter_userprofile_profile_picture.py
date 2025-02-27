# Generated by Django 5.1.2 on 2024-11-09 17:54

import easy_thumbnails.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_remove_userprofile_followers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='static/profile_pictures/', verbose_name='Imagen de perfil'),
        ),
    ]
