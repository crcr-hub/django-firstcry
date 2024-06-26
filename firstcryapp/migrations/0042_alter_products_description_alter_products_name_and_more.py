# Generated by Django 4.2.7 on 2024-02-24 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstcryapp', '0041_alter_variation_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='variation',
            name='eighteentotwentyfourM',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='fourtosixY',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='ninetotwelveM',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='sixtoeightY',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='sixtonineM',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='threetosixM',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='total',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='twelvetoeighteenM',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='twotofourY',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='variation',
            name='zerotothreeM',
            field=models.BigIntegerField(default=0, null=True),
        ),
    ]
