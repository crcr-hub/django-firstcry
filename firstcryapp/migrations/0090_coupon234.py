# Generated by Django 4.2.7 on 2024-04-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0089_delete_return_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='coupon234',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('discount', models.IntegerField(default=0)),
                ('min_amount', models.IntegerField(default=0)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
