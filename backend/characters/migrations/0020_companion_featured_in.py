# Generated by Django 4.0.6 on 2022-10-20 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0019_remove_companion_featured_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='companion',
            name='featured_in',
            field=models.ManyToManyField(blank=True, null=True, to='characters.serial'),
        ),
    ]
