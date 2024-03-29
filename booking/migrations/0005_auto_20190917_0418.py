# Generated by Django 2.2.2 on 2019-09-16 23:48

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('booking', '0004_auto_20190917_0159'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractmodel',
            name='reckoning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='contracts', to='company.ReckoningModel'),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='transfered_at_date',
            field=django_jalali.db.models.jDateField(null=True),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='transfered_at_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='contractmodel',
            name='transfered_to_sportclub',
            field=models.BooleanField(default=False),
        ),
    ]
