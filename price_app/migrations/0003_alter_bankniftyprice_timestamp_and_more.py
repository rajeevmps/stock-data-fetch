# Generated by Django 4.0 on 2024-09-17 06:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('price_app', '0002_alter_bankniftyprice_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankniftyprice',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 9, 17, 11, 38, 24, 250525, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='niftyprice',
            name='timestamp',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2024, 9, 17, 11, 38, 24, 250525, tzinfo=utc)),
        ),
    ]