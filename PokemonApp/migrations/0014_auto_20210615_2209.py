# Generated by Django 3.0.10 on 2021-06-16 02:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PokemonApp', '0013_auto_20210615_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemoncaptured',
            old_name='my_pokemon',
            new_name='specie',
        ),
    ]
