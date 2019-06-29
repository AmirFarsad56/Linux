# Generated by Django 2.1.7 on 2019-05-28 05:54

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0002_salonmodel_safe_keeping'),
        ('session', '0006_auto_20190522_0544'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_length', models.IntegerField(blank=True, null=True)),
                ('last_saturday', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_sunday', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_monday', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_tuesday', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_wednesday', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_thursday', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_friday', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_saturday_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_sunday_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_monday_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_tuesday_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_wednesday_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_thursday_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_friday_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lastdatas', to='salon.SalonModel')),
            ],
        ),
    ]
