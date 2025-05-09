# Generated by Django 5.1.4 on 2025-02-13 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0012_alter_newsletter_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='token',
            field=models.CharField(default='token', max_length=64),
            preserve_default=False,
        ),
    ]
