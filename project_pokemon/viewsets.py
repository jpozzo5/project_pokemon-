from rest_framework import viewsets  ,generics
from rest_framework.views import APIView
from PokemonApp.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated


# class SpritesSerializer(viewsets.ModelViewSet):
# 	queryset = Sprites.objects.all()
# 	serializer_class = SpritesSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    permission_classes = []
    authentication_classes = []

class AreasViewSet(viewsets.ModelViewSet):
    queryset = Areas.objects.all()
    serializer_class = AreasSerializer
    permission_classes = []
    authentication_classes = []
    

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = []
    authentication_classes = []
