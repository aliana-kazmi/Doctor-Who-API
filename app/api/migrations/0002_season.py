# Generated by Django 4.0.6 on 2022-10-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.CreateModel(
                    name='Season',
                    fields=[
                        ('season_no', models.SmallIntegerField(primary_key=True, serialize=False)),
                        ('start_yr', models.DateField()),
                        ('end_yr', models.DateField()),
                    ],
                    options={
                        'db_table': 'characters_season',
                    },
                ),
            ],
            database_operations=[]
        )
    ]
