# Generated by Django 3.0.6 on 2020-05-20 13:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0006_auto_20200519_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 20, 13, 15, 12, 463874, tzinfo=utc)),
        ),
    ]