# Generated by Django 2.1.15 on 2020-11-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('day', models.DateField(db_column='DAY', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'CALENDAR',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReservationCalendar',
            fields=[
                ('reservation_calendar_id', models.AutoField(db_column='RESERVATION_CALENDAR_ID', primary_key=True, serialize=False)),
                ('reservation_count', models.IntegerField(db_column='RESERVATION_COUNT')),
            ],
            options={
                'db_table': 'RESERVATION_CALENDAR',
                'managed': False,
            },
        ),
    ]
