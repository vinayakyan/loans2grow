# Generated by Django 5.0.1 on 2024-01-05 05:42

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='IN')),
                ('message', models.TextField()),
                ('enquiry_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('done', 'done'), ('rejected', 'rejected')], max_length=10)),
                ('response_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]