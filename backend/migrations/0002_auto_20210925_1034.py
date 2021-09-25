# Generated by Django 3.2.7 on 2021-09-25 04:34

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evident',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='evident',
            name='end_at',
        ),
        migrations.AddField(
            model_name='evident',
            name='end_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AddField(
            model_name='evident',
            name='start_datetime',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='evident',
            name='input_values',
            field=models.CharField(blank=True, default='', max_length=200, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]