# Generated by Django 4.2.7 on 2024-04-08 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0065_remove_return_product_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='return_product',
            name='product',
            field=models.ForeignKey(default=31, on_delete=django.db.models.deletion.CASCADE, to='firstcryapp.products'),
        ),
    ]
