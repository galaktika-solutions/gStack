# Generated by Django 2.1.2 on 2018-11-17 12:45

from django.db import migrations
import django_resized.forms
import myuser.models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0002_remove_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=0, size=[150, 150], upload_to=myuser.models.media_file_path, verbose_name='Full Photo'),
        ),
        migrations.AddField(
            model_name='user',
            name='small_photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=0, size=[29, 29], upload_to=myuser.models.media_file_path, verbose_name='Small Photo'),
        ),
    ]
