# Generated by Django 3.1.3 on 2020-12-03 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0005_auto_20201202_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='alert_user',
            options={'ordering': ['user'], 'verbose_name': 'Alert_user', 'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='gender',
            options={'ordering': ['gender'], 'verbose_name': 'Gender', 'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='type_alert',
            options={'ordering': ['alert'], 'verbose_name': 'Type_Alert', 'verbose_name_plural': ''},
        ),
        migrations.AlterModelOptions(
            name='type_animal',
            options={'ordering': ['type'], 'verbose_name': 'Type_animal', 'verbose_name_plural': ''},
        ),
        migrations.AddField(
            model_name='alert_user',
            name='color',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='alert.color'),
            preserve_default=False,
        ),
    ]
