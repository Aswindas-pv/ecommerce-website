# Generated by Django 5.0.2 on 2024-04-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0060_alter_coupon_coupon_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_code',
            field=models.CharField(max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
