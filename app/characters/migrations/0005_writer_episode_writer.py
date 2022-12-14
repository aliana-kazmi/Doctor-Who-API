# Generated by Django 4.0.6 on 2022-10-03 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0004_serial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.AddField(
            model_name='episode',
            name='writer',
            field=models.ManyToManyField(to='characters.writer'),
        ),
    ]
