# Generated by Django 4.2.7 on 2024-02-20 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0022_categories_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zerotothreeM', models.BigIntegerField(default=0)),
                ('threetosixM', models.BigIntegerField(default=0)),
                ('sixtonineM', models.BigIntegerField(default=0)),
                ('ninetotwelveM', models.BigIntegerField(default=0)),
                ('twelvetoeighteenM', models.BigIntegerField(default=0)),
                ('eighteentotwentyfourM', models.BigIntegerField(default=0)),
                ('twotofourY', models.BigIntegerField(default=0)),
                ('fourtosixY', models.BigIntegerField(default=0)),
                ('sixtoeightY', models.BigIntegerField(default=0)),
                ('total', models.BigIntegerField(default=0)),
                ('color', models.CharField(default='Multicolor', max_length=100)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstcryapp.products')),
            ],
        ),
    ]