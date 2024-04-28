# Generated by Django 4.2.7 on 2024-04-03 10:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0054_alter_categories_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Offer_price',
            new_name='total_amount',
        ),
        migrations.RemoveField(
            model_name='order',
            name='deal',
        ),
        migrations.RemoveField(
            model_name='order',
            name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='size',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user_address',
        ),
        migrations.CreateModel(
            name='order_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_address', models.CharField(blank=True, max_length=5000, null=True)),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('deal', models.IntegerField(blank=True, null=True)),
                ('Offer_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='firstcryapp.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstcryapp.products')),
            ],
        ),
    ]
