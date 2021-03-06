# Generated by Django 2.2.16 on 2020-09-10 22:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import functools
import secrets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server', models.GenericIPAddressField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiry', models.DateTimeField(default=datetime.datetime(2020, 9, 10, 22, 24, 55, 676280, tzinfo=utc))),
                ('secret', models.CharField(db_index=True, default=functools.partial(secrets.token_urlsafe, *(32,), **{}), max_length=100, unique=True)),
            ],
        ),
    ]
