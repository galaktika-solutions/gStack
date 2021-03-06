# Generated by Django 2.2.9 on 2020-03-22 13:58

from django.db import migrations, models
import django.db.models.deletion
import email_backend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentEmails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=1000, verbose_name='Email subject')),
                ('body', models.TextField(blank=True, verbose_name='Email body')),
                ('from_address', models.TextField()),
                ('to_address', models.TextField()),
                ('cc_address', models.TextField(blank=True)),
                ('bcc_address', models.TextField(blank=True)),
                ('content_subtype', models.CharField(default='html', max_length=10)),
                ('sent_at', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Sent Emails',
            },
        ),
        migrations.CreateModel(
            name='SentEmailsAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(max_length=1000, upload_to=email_backend.models.media_file_path)),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('sent_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='email_backend.SentEmails')),
            ],
        ),
    ]
