# Generated by Django 3.0.10 on 2021-06-16 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PokemonApp', '0002_auto_20210616_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemoncaptured',
            name='nick_name',
            field=models.CharField(max_length=40, verbose_name='Nick Name'),
        ),
    ]
