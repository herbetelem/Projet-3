# Generated by Django 3.1.3 on 2020-12-02 16:36

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alert', '0005_auto_20201202_1613'),
        ('housing', '0003_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserData',
            new_name='User_data',
        ),
    ]