# Generated by Django 2.2.2 on 2019-07-26 22:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20190727_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profitpercentagemodel',
            old_name='profit_percantage',
            new_name='profit_percentage',
        ),
    ]
