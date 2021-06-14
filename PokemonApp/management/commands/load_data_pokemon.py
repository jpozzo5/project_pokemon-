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
        abilities_ids = [abilities_obj.filter(name=ab) if abilities_obj.filter(name=ab)else \
             abilities_obj.create(name=ab) for ab in abilities ]
        return abilities_ids

    def get_or_create_moves(self,moves):
        moves_obj = Moves.objects
        moves_ids = [moves_obj.filter(name=mv) if moves_obj.filter(name=mv) else \
             moves_obj.create(name=mv) for mv in moves ]
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
        )

        return Sprites.objects.filter(pk=sprites_obj.id)
    def get_or_create_stats(self,stats):
        stats_obj = Stats.objects
        stats_ids = [stats_obj.filter(name=st['name']) if stats_obj.filter(name=st) else \
             stats_obj.create(name=st['name'],value=st['value'] ) for st in stats ]
        
        return stats_ids   
    
    def get_or_create_types(self,types):
        type_obj = Types.objects
        abilities_ids = [type_obj.filter(name=tp) if type_obj.filter(name=tp) else \
             type_obj.create(name=tp) for tp in types ]
        return abilities_ids


    def loads_pokemons(self,ctx):
        pokemon_obj = Pokemon.objects
        for data in ctx['data']:
            #we create the pokemon first with the basic attributes
            
            pokemon_new = pokemon_obj.create(
                            capture_rate = data['capture_rate'],
                            color = data['color'],
                            flavor_text = data['flavor_text'],
                            height = data['height'],
                            name= data['name'],
                            weight= data['weight'],
                            )
            pokemon_new = pokemon_obj.get(pk = pokemon_new.id)

            abilities = self.get_or_create_abilities(data['abilities'])

            for ab in abilities:
                for i in ab:
                    if not pokemon_new.abilities.filter(pk =int(i.id)):
                        pokemon_new.abilities.add(int(i.id))

            moves = self.get_or_create_moves(data['moves'])
            for mv in moves:
                for i in mv:
                    if not pokemon_new.moves.filter(pk =int(i.id)):
                        pokemon_new.moves.add(int(i.id))

            
            sprites = self.get_or_create_sprites(data['sprites'])
            for sp in sprites:
                if not pokemon_new.sprites.filter(pk =int(sp.id)):
                    pokemon_new.sprites.add(int(i.id))
            
            stats = self.get_or_create_stats(data['stats']) 
            
            for st in stats:
                if not pokemon_new.stats.filter(pk =int(st.id)):
                    pokemon_new.stats.add(int(i.id))

            type = self.get_or_create_types(data['types']) 
            for ty in type:
                for i in ty:
                    print(i)
                    if not pokemon_new.types.filter(pk =int(i.id)):
                        pokemon_new.types.add(int(i.id))


        return
    #This is the main method, which calls the secondary methods to perform the data load.
    def handle(self, *args, **options):
        for file_name in _FILES:     
            ctx =self.load_text(file_name)
            if file_name == 'pokemons.json':
                self.loads_pokemons(ctx)



