# Generated by Django 4.2.7 on 2024-02-20 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0027_variation_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='colors',
        ),
        migrations.DeleteModel(
            name='color',
        ),
    ]
