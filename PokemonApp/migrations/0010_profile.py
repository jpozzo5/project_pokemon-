# Generated by Django 3.0.10 on 2021-06-14 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PokemonApp', '0009_auto_20210614_0817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=40, verbose_name='Nick Name')),
                ('is_party_member', models.BooleanField()),
                ('my_pokemons', models.ManyToManyField(related_name='Pokemons', to='PokemonApp.Pokemon')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
