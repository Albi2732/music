# Generated by Django 4.1.4 on 2023-06-16 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0021_remove_song_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='movie',
            field=models.CharField(default='', max_length=500, verbose_name='Видео'),
        ),
    ]
