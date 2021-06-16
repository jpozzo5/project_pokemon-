from typing import Type
from django.core.management import BaseCommand
from PokemonApp.models import *
import os
import json
import logging
_logger = logging.getLogger(__name__)

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(os.path.sep, PROJECT_DIR, "static", "json")
_FILES = ['pokemons.json','areas.json','locations.json','regions.json']

"""
    This is a command created using the framework tools to import the data that is in the flat files.
"""
class Command(BaseCommand):
    def load_text(self,textname):
        with open(os.path.join(BASE_DIR, textname), 'r') as js:
            js = json.load(js)
        return js
    
    def get_or_create_abilities(self,abilities):
        abilities_obj = Abilities.objects
        abilities_ids = []
        for ab in abilities :
            if abilities_obj.filter(name=ab):
                for i in abilities_obj.filter(name=ab):
                    abilities_ids.append(i)
            else:
                abilities_obj.create(name=ab)
                for i in abilities_obj.filter(name=ab):
                    abilities_ids.append(i)

        return abilities_ids

    def get_or_create_moves(self,moves):
        moves_obj = Moves.objects
        moves_ids = []
        for mv in moves :
            if moves_obj.filter(name=mv):
                for i in moves_obj.filter(name=mv):
                    moves_ids.append(i)
            else:
                moves_obj.create(name=mv)
                for i in moves_obj.filter(name=mv):
                    moves_ids.append(i)
        return moves_ids   

    def get_or_create_sprites(self,sprites):
        sprites_obj = Sprites.objects.create(
            back_default=sprites['back_default'],
            back_female=sprites['back_female'],
            back_shiny=sprites['back_shiny'],
            back_shiny_female=sprites['back_shiny_female'],
            front_female=sprites['front_female'],
            front_shiny=sprites['front_shiny'],
            front_shiny_female =sprites['front_shiny_female'],
            front_default =  sprites['front_default']
        )

        return Sprites.objects.get(pk=sprites_obj.id)
    def get_or_create_stats(self,stats):
        stats_obj = Stats.objects
        stats_ids = [stats_obj.filter(name=st['name']) if stats_obj.filter(name=st) else \
             stats_obj.create(name=st['name'],value=st['value'] ) for st in stats ]
        
        return stats_ids   
    
    def get_or_create_types(self,types):
        type_obj = Types.objects
        types_ids = []
        for tp in types :
            if type_obj.filter(name=tp):
                for i in type_obj.filter(name=tp):
                    types_ids.append(i)
            else:
                type_obj.create(name=tp)
                for i in type_obj.filter(name=tp):
                    types_ids.append(i)
        return types_ids


    def loads_pokemons(self,ctx):
        pokemon_obj = Pokemon.objects
        for data in ctx['data']:
            #we create the pokemon first with the basic attributes
            sprites = self.get_or_create_sprites(data['sprites'])
            pokemon_new = pokemon_obj.create(
                            capture_rate = data['capture_rate'],
                            color = data['color'],
                            flavor_text = data['flavor_text'],
                            height = data['height'],
                            name= data['name'],
                            weight= data['weight'],
                            sprites = sprites,
                            )
            pokemon_new = pokemon_obj.get(pk = pokemon_new.id)

            abilities = self.get_or_create_abilities(data['abilities'])

            if abilities:
                for ab in abilities:
                    if not pokemon_new.abilities.filter(pk =ab.id):
                        pokemon_new.abilities.add(ab.id)

            moves = self.get_or_create_moves(data['moves'])
            if moves:
                for mv in moves:
                    if not pokemon_new.moves.filter(pk =mv.id):
                        pokemon_new.moves.add(mv.id)

            stats = self.get_or_create_stats(data['stats']) 
            for st in stats:
                if not pokemon_new.stats.filter(pk =int(st.pk)):
                    pokemon_new.stats.add(int(st.pk))

            type = self.get_or_create_types(data['types']) 
            for ty in type:
                if not pokemon_new.types.filter(pk =ty.id):
                    pokemon_new.types.add(ty.id)
        return
    #This is the main method, which calls the secondary methods to perform the data load.
    def handle(self, *args, **options):
        for file_name in _FILES:     
            ctx =self.load_text(file_name)
            if file_name == 'pokemons.json':
                self.loads_pokemons(ctx)



