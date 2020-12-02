# Generated by Django 3.1.3 on 2020-12-01 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0003_auto_20201201_1133'),
        ('housing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert_user',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.animal'),
        ),
        migrations.AddField(
            model_name='alert_user',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.gender'),
        ),
        migrations.AddField(
            model_name='alert_user',
            name='type_alert',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.type_alert'),
        ),
        migrations.AddField(
            model_name='alert_user',
            name='type_animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.type_animal'),
        ),
        migrations.AddField(
            model_name='alert_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='housing.user'),
        ),
    ]
