# Generated by Django 4.2.7 on 2024-03-01 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0042_alter_products_description_alter_products_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variation',
            name='product',
        ),
        migrations.AddField(
            model_name='products',
            name='varient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='firstcryapp.variation'),
        ),
    ]
