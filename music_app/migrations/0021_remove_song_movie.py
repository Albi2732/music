# Generated by Django 4.1.4 on 2023-06-16 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0020_alter_history_options_alter_likedsong_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='movie',
        ),
    ]
