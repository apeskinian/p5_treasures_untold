# Generated by Django 5.1.4 on 2025-02-07 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_realm_the_prefix_required'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='unique_stock',
            field=models.BooleanField(default=False),
        ),
    ]
