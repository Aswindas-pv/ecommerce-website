# Generated by Django 5.0.2 on 2024-03-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0010_alter_product_back_view_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_listed',
            field=models.BooleanField(default=True),
        ),
    ]