from django.db import models
from django.conf import settings

#-------------------------------------------Models for Pokemons

#Pokemon skills this is related in the Pokemon model with a many2many. 
class Abilities(models.Model):
    name = models.CharField('Name', max_length=100)
    def __str__(self):
        return f'{self.name}'

# Pokemon Moves this is related in the Pokemon model with a many2many. 

class Moves(models.Model):
    name = models.CharField('Name', max_length=100)
    def __str__(self):
        return f'{self.name}'



class Stats(models.Model):
    name = models.CharField('Name', max_length=100)
    value = models.IntegerField()
    def __str__(self):
        return '{0}:{1}{2}'.format('stats', self.name, self.value)

class Types(models.Model):
    name = models.CharField('Name', max_length=100)
    def __str__(self):
        return f'{self.name}'

class Sprites(models.Model):
    back_shiny = models.URLField("back shiny", 
        max_length=300, 
        db_index=True, 
        blank=True, null=True
    )

    back_female =  models.URLField("back female", 
        max_length=300, 
        db_index=True, 
        blank=True, null=True
        
    )
    front_shiny = models.URLField("front shiny", 
        max_length=300, 
        db_index=True, 
        blank=True, null=True

    )
    back_default = models.URLField("Back Default", 
        max_length=300, 
        db_index=True, 

        blank=True, null=True
    )
    front_female = models.URLField("Front Female", 
        max_length=300, 
        db_index=True, 

        blank=True, null=True
    )
    front_default = models.URLField("front default", 
        max_length=300, 
        db_index=True, 
  
        blank=True, null=True
    )
    back_shiny_female = models.URLField("back shiny female", 
        max_length=300, 
        db_index=True, 

        blank=True, null=True
    )
    front_shiny_female = models.URLField("front shiny female", 
        max_length=300, 
        db_index=True, 
        blank=True, null=True
    )
    def __str__(self):
        return f'Sprites for:{self.pokemon_set.name}'




#Main model of a pokemon.
class Pokemon(models.Model):
    abilities = models.ManyToManyField(Abilities, related_name='Abilities')
    capture_rate = models.FloatField('Capture Rate',null=True)
    color = models.CharField('Color', max_length=20)
    flavor_text = models.TextField('flavor text')
    height = models.FloatField('Height',null=True)
    moves = models.ManyToManyField(Moves, related_name='Moves')
    name = models.CharField('Name', max_length=30)
    sprites = models.ForeignKey(Sprites ,on_delete=models.CASCADE)
    stats = models.ManyToManyField(Stats, related_name='Stats')
    types = models.ManyToManyField(Types, related_name='Types')
    weight = models.FloatField('Weight',null=True)

    def __str__(self):
        return f'{self.name}'
#---------EndModelsForPokemons

#-------------ModelsForRegions


class Location(models.Model):
    name = models.CharField('name', max_length=40)
    def __str__(self):
        return f'{self.name}'



class Areas(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField('name', max_length = 50)
    pokemons = models.ManyToManyField(Pokemon, related_name='Pokemon')

    
class Region(models.Model):
    name = models.CharField('name', max_length=30)
    location = models.ManyToManyField(Location, related_name='Location')






#-------------EndModelsForRegions


class PokemonCaptured(models.Model):
    # nick_name = models.OneToOneField(settings.AUTH_USER_MODEL,
    #                             on_delete=models.CASCADE)
    nick_name = models.CharField('Nick Name', max_length=40)
    specie = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    is_party_member = models.BooleanField()
    
    def __str__(self):
        return f'{self.nick_name}'


