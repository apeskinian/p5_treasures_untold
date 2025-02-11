# Generated by Django 5.1.4 on 2025-02-10 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_alter_faqs_options_alter_faqstopics_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faqs',
            options={'ordering': ['sort_order'], 'verbose_name_plural': 'FAQs'},
        ),
        migrations.AddField(
            model_name='faqs',
            name='sort_order',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
