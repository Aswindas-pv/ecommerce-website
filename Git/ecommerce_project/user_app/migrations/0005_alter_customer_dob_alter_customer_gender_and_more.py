# Generated by Django 5.0.2 on 2024-04-30 04:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0004_customer_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.IntegerField(blank=True, choices=[(1, 'Male'), (2, 'Female'), (3, 'Other')], default=3, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must have 10 digits.', regex='^\\d{10}$')]),
        ),
    ]
