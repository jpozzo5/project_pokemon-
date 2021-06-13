from django.contrib import admin

from .models import *



@admin.register(Abilities)
class AbilitiesAdmin(admin.ModelAdmin):
    list_display= ['name']

@admin.register(Moves)
class Moves(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Sprites)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['back_shiny','back_female','front_shiny','back_default','front_female','front_default','back_shiny_female','front_shiny_female']

@admin.register(Stats)
class Stats(admin.ModelAdmin):
    list_display = ['name','value',]

@admin.register(Types)
class Types(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Pokemon)
class Pokemon(admin.ModelAdmin):
    list_display = ['color','height','name',]



@admin.register(Region)
class Region(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Areas)
class Areas(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Location)
class Location(admin.ModelAdmin):
    list_display = ['name',]
