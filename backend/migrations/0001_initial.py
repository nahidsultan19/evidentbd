# Generated by Django 3.2.7 on 2021-09-25 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_values', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
