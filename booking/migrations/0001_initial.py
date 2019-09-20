# Generated by Django 2.2.2 on 2019-09-15 14:42

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('commonuser', '0001_initial'),
        ('session', '0001_initial'),
        ('salon', '0001_initial'),
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfitPercentageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_percentage', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ContractModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at_date', django_jalali.db.models.jDateField()),
                ('str_created_at_date', models.CharField(max_length=264)),
                ('created_at_time', models.TimeField()),
                ('total_price', models.FloatField()),
                ('numbers', models.IntegerField()),
                ('booker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='commonuser.CommonUserModel')),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='salon.SalonModel')),
            ],
        ),
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfered_to_sportclub', models.BooleanField(default=False)),
                ('transfered_at_date', django_jalali.db.models.jDateField(null=True)),
                ('transfered_at_time', models.TimeField(null=True)),
                ('booked_at_date', django_jalali.db.models.jDateField()),
                ('booked_at_time', models.TimeField()),
                ('final_price', models.FloatField()),
                ('discount_percentage', models.IntegerField()),
                ('company_discount_percentage', models.IntegerField()),
                ('raw_price', models.FloatField()),
                ('profit_percantage', models.IntegerField()),
                ('company_portion', models.FloatField()),
                ('sportclub_portion', models.FloatField(blank=True, null=True)),
                ('cancelled', models.BooleanField(default=False)),
                ('is_contract', models.BooleanField(default=False)),
                ('contract_discount', models.IntegerField(null=True)),
                ('code', models.CharField(max_length=264)),
                ('pay_back', models.FloatField(null=True)),
                ('cancelled_at_date', django_jalali.db.models.jDateField(null=True)),
                ('cancelled_at_time', models.TimeField(null=True)),
                ('booker', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='commonuser.CommonUserModel')),
                ('reckoning', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='company.ReckoningModel')),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='salon.SalonModel')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='session.SessionModel')),
            ],
        ),
    ]
