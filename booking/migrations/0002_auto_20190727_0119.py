# Generated by Django 2.2.2 on 2019-07-26 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommissionModel',
            new_name='ProfitPercentageModel',
        ),
    ]
