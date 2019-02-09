# Generated by Django 2.1.3 on 2019-02-09 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sql', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_run_date', models.DateTimeField(auto_now=True)),
                ('snapshot', models.BooleanField(default=False, help_text='Include in snapshot task (if enabled)')),
                ('connection', models.CharField(blank=True, help_text='Name of DB connection (as specified in settings) to use for this query. Will use EXPLORER_DEFAULT_CONNECTION if left blank', max_length=128, null=True)),
                ('created_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Queries',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='QueryLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sql', models.TextField(blank=True, null=True)),
                ('run_at', models.DateTimeField(auto_now_add=True)),
                ('duration', models.FloatField(blank=True, null=True)),
                ('connection', models.CharField(blank=True, max_length=128, null=True)),
                ('query', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='explorer.Query')),
                ('run_by_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-run_at'],
            },
        ),
    ]
