# Generated by Django 5.1.2 on 2024-11-16 17:53

import easy_thumbnails.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=easy_thumbnails.fields.ThumbnailerImageField(upload_to='posts_images/', verbose_name='Imagen'),
        ),
    ]
