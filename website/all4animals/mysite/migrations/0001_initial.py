# Generated by Django 3.1.3 on 2020-11-25 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=70)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=400)),
                ('postal_code', models.IntegerField()),
                ('host', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Housing_planning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type_animal', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.user')),
            ],
        ),
    ]