from rest_framework import viewsets
from PokemonApp.models import *
from .serializers import PokemonSerializer ,SpritesSerializer

# class SpritesSerializer(viewsets.ModelViewSet):
# 	queryset = Sprites.objects.all()
# 	serializer_class = SpritesSerializer

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
