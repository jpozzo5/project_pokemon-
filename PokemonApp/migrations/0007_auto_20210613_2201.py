# Generated by Django 3.0.10 on 2021-06-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokemonApp', '0006_auto_20210613_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=40, verbose_name='name'),
        ),
    ]