# Generated by Django 4.2.7 on 2023-11-30 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0003_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='prod_image')),
                ('description', models.CharField(max_length=500)),
                ('necktype', models.CharField(max_length=50)),
                ('sleevetype', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('deal', models.IntegerField(blank=True, null=True)),
                ('Offer_price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('gender', models.CharField(max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('qnty', models.IntegerField(null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstcryapp.categories')),
            ],
        ),
    ]
