# Generated by Django 4.2.7 on 2023-12-04 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0013_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='qnty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]