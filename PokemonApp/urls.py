from django.urls import path
from django.conf.urls import url, include
from PokemonApp.views import *
from rest_framework.routers import SimpleRouter
from project_pokemon.viewsets import *
router = SimpleRouter()
router.register(r'pokemons',PokemonViewSet )
router.register(r'regions',RegionViewSet )
router.register(r'areas',AreasViewSet )
router.register(r'locations',LocationViewSet )
urlpatterns = [
    #path("home", Home, name="home"),
    url(r'^', include(router.urls)),
]