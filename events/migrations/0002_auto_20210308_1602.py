# Generated by Django 3.1.7 on 2021-03-08 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='event',
            name='start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]