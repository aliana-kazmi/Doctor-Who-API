# Generated by Django 4.0.6 on 2022-10-06 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0013_remove_episode_writer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='episode',
            name='season',
        ),
    ]