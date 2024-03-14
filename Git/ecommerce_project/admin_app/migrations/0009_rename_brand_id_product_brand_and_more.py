# Generated by Django 5.0.2 on 2024-03-14 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0008_alter_brand_manufacturer_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='brand_id',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_id',
            new_name='category',
        ),
        migrations.AlterField(
            model_name='product',
            name='main_image',
            field=models.FileField(upload_to='media/product_images/'),
        ),
    ]