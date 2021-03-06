# Generated by Django 2.2.9 on 2020-03-15 10:05

from django.db import migrations
import easy_thumbnails.fields
import myuser.models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_remove_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to=myuser.models.media_file_path, verbose_name='Full Photo'),
        ),
        migrations.AddField(
            model_name='user',
            name='small_photo',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, upload_to=myuser.models.media_file_path, verbose_name='Small Photo'),
        ),
    ]
