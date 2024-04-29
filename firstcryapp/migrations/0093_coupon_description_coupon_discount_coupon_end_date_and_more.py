# Generated by Django 4.2.7 on 2024-04-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0092_remove_coupon_description_remove_coupon_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='min_amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coupon',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]