# Generated by Django 3.1.3 on 2021-01-09 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0008_auto_20210108_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_user',
            name='street',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
