# Generated by Django 2.2.2 on 2019-09-15 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingmodel',
            name='reckoning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='company.ReckoningModel'),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='sportclub_portion',
            field=models.FloatField(default=2500.0),
            preserve_default=False,
        ),
    ]