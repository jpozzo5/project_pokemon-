from django.urls import path
from django.conf.urls import url, include
from PokemonApp.views import *
from rest_framework.routers import SimpleRouter
from project_pokemon.viewsets import PokemonViewSet
router = SimpleRouter()
router.register(r'pokemons',PokemonViewSet )
urlpatterns = [
    #path("home", Home, name="home"),
    url(r'^', include(router.urls)),
]