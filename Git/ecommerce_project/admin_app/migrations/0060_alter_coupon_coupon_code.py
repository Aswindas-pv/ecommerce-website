# Generated by Django 5.0.2 on 2024-04-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_app", "0059_rename_coupon_price_coupon_maximum_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coupon",
            name="coupon_code",
            field=models.CharField(primary_key=True, serialize=False, unique=True),
        ),
    ]
