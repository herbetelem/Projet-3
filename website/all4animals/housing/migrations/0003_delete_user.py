# Generated by Django 3.1.3 on 2020-12-02 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_auto_20201202_1613'),
        ('alert', '0005_auto_20201202_1613'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
