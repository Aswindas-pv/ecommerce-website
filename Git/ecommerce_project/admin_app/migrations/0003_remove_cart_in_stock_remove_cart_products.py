# Generated by Django 5.0.2 on 2024-03-27 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0002_alter_cart_customer_alter_wishlist_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='in_stock',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
    ]