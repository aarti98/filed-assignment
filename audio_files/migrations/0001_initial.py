# Generated by Django 3.2.3 on 2021-05-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudiobookAudioFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PodcastAudioFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField()),
                ('host', models.CharField(max_length=100)),
                ('participants', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SongAudioFileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.PositiveIntegerField()),
                ('uploaded_time', models.DateTimeField()),
            ],
        ),
    ]
