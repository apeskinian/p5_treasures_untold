# Generated by Django 5.1.4 on 2025-04-01 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_realm_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realm',
            name='name',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
