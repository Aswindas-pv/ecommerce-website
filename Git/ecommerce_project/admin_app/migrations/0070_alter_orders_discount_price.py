# Generated by Django 5.0.2 on 2024-04-22 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0069_remove_wallettransaction_order_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='discount_price',
            field=models.PositiveBigIntegerField(blank=True, default=0),
        ),
    ]
