# Generated by Django 4.2.7 on 2024-02-20 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0026_remove_variation_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='variation',
            name='colors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='firstcryapp.color'),
        ),
    ]
