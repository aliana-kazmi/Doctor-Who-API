# Generated by Django 4.0.6 on 2022-10-07 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0014_remove_episode_season'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='original_air_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
