# Generated by Django 5.0.2 on 2024-03-11 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_deleted'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='deleted',
            new_name='is_deleted',
        ),
    ]
