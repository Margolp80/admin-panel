# Generated by Django 3.1.7 on 2021-03-08 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20210308_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2015, 10, 9, 23, 55, 59, 342380)),
        ),
    ]
