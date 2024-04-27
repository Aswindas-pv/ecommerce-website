# Generated by Django 5.0.2 on 2024-04-27 13:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0073_categoryoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryoffer',
            name='category',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='categoryoffer', to='admin_app.category'),
        ),
    ]