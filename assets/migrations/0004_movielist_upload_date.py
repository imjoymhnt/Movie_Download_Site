# Generated by Django 3.0.6 on 2020-05-19 08:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20200519_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.date(2020, 5, 19)),
        ),
    ]
