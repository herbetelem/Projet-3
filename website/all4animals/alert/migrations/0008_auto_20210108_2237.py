# Generated by Django 3.1.3 on 2021-01-08 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0007_auto_20201203_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='alert_user',
            options={'ordering': ['user'], 'verbose_name': 'Alert user', 'verbose_name_plural': 'Les alertes utilisateurs'},
        ),
    ]