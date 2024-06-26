# Generated by Django 5.0.2 on 2024-05-01 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_app", "0076_alter_orders_discount_price"),
    ]

    operations = [
        migrations.CreateModel(
            name="Banner",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="orderitem",
            name="request_cancel",
            field=models.BooleanField(default=False),
        ),
    ]
