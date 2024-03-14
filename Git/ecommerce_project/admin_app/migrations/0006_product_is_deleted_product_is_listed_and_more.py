# Generated by Django 5.0.2 on 2024-03-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_rename_products_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='is_listed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='back_view_image',
            field=models.ImageField(default=1, upload_to='media/product_images/'),
            preserve_default=False,
        ),
    ]