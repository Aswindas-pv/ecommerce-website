# Generated by Django 5.0.2 on 2024-04-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0036_remove_orderitem_return_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='return_product',
            field=models.BooleanField(default=False),
        ),
    ]