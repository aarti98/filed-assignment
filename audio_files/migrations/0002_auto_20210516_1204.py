# Generated by Django 3.2.3 on 2021-05-16 12:04

import audio_files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobookaudiofilemodel',
            name='uploaded_time',
            field=models.DateTimeField(validators=[audio_files.models.validate_datetime]),
        ),
        migrations.AlterField(
            model_name='podcastaudiofilemodel',
            name='uploaded_time',
            field=models.DateTimeField(validators=[audio_files.models.validate_datetime]),
        ),
        migrations.AlterField(
            model_name='songaudiofilemodel',
            name='uploaded_time',
            field=models.DateTimeField(validators=[audio_files.models.validate_datetime]),
        ),
    ]
