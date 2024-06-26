# Generated by Django 4.2.7 on 2024-04-08 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0062_alter_order_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='return_product',
            name='reason',
        ),
        migrations.AddField(
            model_name='return_product',
            name='product',
            field=models.ForeignKey(blank=True, default='de', on_delete=django.db.models.deletion.CASCADE, to='firstcryapp.products'),
        ),
        migrations.AddField(
            model_name='return_product',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='return_product',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='return_product',
            name='stock_status',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='return_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=1000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='firstcryapp.order')),
            ],
        ),
    ]
