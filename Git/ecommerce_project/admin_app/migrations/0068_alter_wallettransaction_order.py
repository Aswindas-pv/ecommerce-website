# Generated by Django 5.0.2 on 2024-04-22 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_app", "0067_wallettransaction_order"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wallettransaction",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="admin_app.orders",
            ),
        ),
    ]
