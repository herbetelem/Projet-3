# Generated by Django 3.1.5 on 2021-01-12 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0010_alert_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert_user',
            name='img',
            field=models.TextField(max_length=300),
        ),
    ]
