# Generated by Django 2.2.16 on 2020-09-11 20:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20200911_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='expiry',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 11, 20, 51, 3, 469501, tzinfo=utc)),
        ),
    ]
