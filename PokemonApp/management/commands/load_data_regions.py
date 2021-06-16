from django.core.management import BaseCommand
from PokemonApp.models import *
import os
import json
import logging
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.join(os.path.sep, PROJECT_DIR, "static", "json")
_logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def load_text(self,textname):
        with open(os.path.join(BASE_DIR, textname), 'r') as js:
            js = json.load(js)
        return js
    def handle(self, *args, **options):    
        ctx = self.load_text('regions.json')
        i = 0
        for region in ctx['data']:           
            if not Region.objects.filter(name = region['name']):
                region_obj = Region.objects.create(name = region['name'])
                region_obj2 = Region.objects.get(pk = region_obj.id)
                for location in region['locations']:
                    location_obj = Location.objects.filter(name = location)        
                    if location_obj.exists():
                        for location in location_obj:
                            region_obj2.location.add(location.id)







