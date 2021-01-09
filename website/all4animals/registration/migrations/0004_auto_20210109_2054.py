# Generated by Django 3.1.3 on 2021-01-09 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_user_data_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_data',
            name='address',
        ),
        migrations.AddField(
            model_name='user_data',
            name='city',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user_data',
            name='street',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
