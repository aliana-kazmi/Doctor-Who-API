# Generated by Django 4.0.6 on 2022-10-22 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0028_villain'),
    ]

    operations = [
        migrations.AddField(
            model_name='villain',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]