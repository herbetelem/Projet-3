# Generated by Django 3.1.5 on 2021-01-18 19:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                'verbose_name_plural': 'Couleurs',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': "Sexe de l'animal",
                'ordering': ['gender'],
            },
        ),
        migrations.CreateModel(
            name='Type_alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alert', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Type Alert',
                'verbose_name_plural': "Type d'alerte",
                'ordering': ['alert'],
            },
        ),
        migrations.CreateModel(
            name='Type_animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Type animal',
                'verbose_name_plural': "Type d'animal",
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Alert_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=70)),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('date', models.DateField(max_length=300)),
                ('commentary', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.color')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.gender')),
                ('type_alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.type_alert')),
                ('type_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alert.type_animal')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Alert user',
                'verbose_name_plural': 'Les alertes utilisateurs',
                'ordering': ['user'],
            },
        ),
    ]
