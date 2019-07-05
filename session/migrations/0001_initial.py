# Generated by Django 2.2.2 on 2019-07-01 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saturdays', models.BooleanField(default=False)),
                ('sundays', models.BooleanField(default=False)),
                ('mondays', models.BooleanField(default=False)),
                ('tuesdays', models.BooleanField(default=False)),
                ('wednesdays', models.BooleanField(default=False)),
                ('thursdays', models.BooleanField(default=False)),
                ('fridays', models.BooleanField(default=False)),
                ('range_start_day', django_jalali.db.models.jDateField()),
                ('range_end_day', django_jalali.db.models.jDateField()),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessioncategories', to='salon.SalonModel')),
            ],
        ),
        migrations.CreateModel(
            name='SessionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', django_jalali.db.models.jDateField(null=True)),
                ('time', models.TimeField(null=True)),
                ('duration', models.CharField(max_length=264)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('is_ready', models.BooleanField(default=False)),
                ('booker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to=settings.AUTH_USER_MODEL)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='salon.SalonModel')),
                ('session_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='session.SessionCategoryModel')),
            ],
        ),
        migrations.CreateModel(
            name='LastDataModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_length', models.IntegerField(blank=True, null=True)),
                ('first_day', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('first_day_2', django_jalali.db.models.jDateField(blank=True, null=True)),
                ('last_day', django_jalali.db.models.jDateField(blank=True, null=True)),
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
