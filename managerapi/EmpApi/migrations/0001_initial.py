# Generated by Django 2.2.16 on 2020-12-19 06:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('company', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')])),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['firstname', 'lastname'],
            },
        ),
    ]
