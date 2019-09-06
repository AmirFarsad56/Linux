# Generated by Django 2.2.2 on 2019-09-02 11:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonUserModel',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='commonusers', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_number', models.CharField(max_length=20, null=True)),
                ('picture', models.ImageField(default='commonuser/default/default_commonuser.jpg', upload_to='commonuser/coverpicture')),
            ],
        ),
    ]
