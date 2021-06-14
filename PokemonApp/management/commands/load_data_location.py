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
        ctx =self.load_text('locations.json')
        for location in ctx['data']:
            if not Location.objects.filter(name = location['name']):
                Location.objects.create(name = location['name'])


