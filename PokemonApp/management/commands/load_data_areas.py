from django.core.management import BaseCommand
from PokemonApp.models import *
import os
import json
import logging
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(os.path.sep, PROJECT_DIR, "static", "json")
_logger = logging.getLogger(__name__)

"""
This command will allow us to import all the Areas. 
Important data must be loaded the locations and regions
"""
class Command(BaseCommand):
    def load_text(self,textname):
        with open(os.path.join(BASE_DIR, textname), 'r') as js:
            js = json.load(js)
        return js
    def handle(self, *args, **options):   
        ctx =self.load_text('areas.json')
        i =0
        for areas in ctx['data']:
            area_obj = Areas.objects.filter(name =areas['name']).exists()
            if not area_obj:
                location = Location.objects.filter(name = areas['location']).exists()
                if location:
                    location = Location.objects.get(name = areas['location'])
                    area_obj = Areas.objects.create(name =areas['name'],location =location)
                    area_obj = Areas.objects.get(pk = area_obj.id)
                    for pokemon in areas['pokemons']:
                        #lleva esta consulta porque cuando se importan los pokemon la inicial de la palabra esta en mayuscula
                        pokemon_obj = Pokemon.objects.filter(name__iexact = pokemon)
                        if pokemon_obj.exists():
                            for pok in pokemon_obj:
                                area_obj.pokemons.add(pok.id)