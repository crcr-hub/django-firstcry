# Generated by Django 4.2.7 on 2024-03-30 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0049_remove_order_total_price_order_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='mobile',
            field=models.BigIntegerField(default=0),
        ),
    ]
