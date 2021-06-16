from django.urls import path
from django.conf.urls import url, include
from PokemonApp.views import *
from rest_framework.routers import SimpleRouter
from project_pokemon.viewsets import *

router = SimpleRouter()
#router.register(r'^pokemons',PokemonViewSet )
router.register(r'regions',RegionViewSet )
router.register(r'areas',AreasViewSet )
router.register(r'locations',LocationViewSet )

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^pokemons/$', PokemonsListRestView.as_view(),name ="pokemon_list"),
    url(r'^pokemons/(?P<pk>\d+)', PokemonsRestView.as_view(),name ="pokemon_id"),
    url(r'^pokemons/own/$', PokemonsCapturedRestView.as_view(),name ="own"),
    url(r'^test/$', TestRestView.as_view(),name ="test"),

    
]