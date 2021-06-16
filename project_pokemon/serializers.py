from rest_framework import serializers

from PokemonApp.models import *

class SpritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprites
        fields = ('back_shiny', 'back_female','front_shiny', 'back_default','front_female', 'front_default','back_shiny_female', 'front_shiny_female')
    def create(self, validated_data):
        return Sprites.objects.create(**validated_data)  

class StatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stats
        fields = ('name', 'value')
    def create(self, validated_data):
        return Stats.objects.create(**validated_data)  

class PokemonSerializer(serializers.ModelSerializer):
    abilities = serializers.StringRelatedField(many=True, read_only=True)
    capture_rate = serializers.FloatField()
    color = serializers.StringRelatedField()
    flavor_text = serializers.StringRelatedField()
    height = serializers.FloatField()
    moves = serializers.StringRelatedField(many=True, read_only=True)
    name = serializers.StringRelatedField()
    sprites = SpritesSerializer()
    stats =  StatsSerializer(many=True)
    types = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = '__all__'

#-----------------------------------------------------------------------------
class RegionSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Region
        fields = ('name', 'location')
    def create(self, validated_data):
        return Region.objects.create(**validated_data)

class RegionSerializer2(serializers.ModelSerializer):
    location = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Region
        fields = ('name', 'location')
    def create(self, validated_data):
        return Region.objects.create(**validated_data)

class AreasSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField()
    pokemons = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Areas
        fields = ('location','name','pokemons')
    def create(self, validated_data):
        return Areas.objects.create(**validated_data)


class LocationSerializer(serializers.ModelSerializer):
    sprites = SpritesSerializer(many=True, read_only=True)
    areas = serializers.SerializerMethodField()
    def get_areas(self, obj):
        for c in obj.areas_set.all():
            ctx = { 'id':c.id,
                    'name':c.name,
                    'pokemons_count':len(c.pokemons.all()),
                    'location':c.location.id
            }
            return ctx

    class Meta:
        model = Location
        fields = '__all__'
    def create(self, validated_data):
        return Location.objects.create(**validated_data)




class CapturePSerializer(serializers.ModelSerializer):
    specie = serializers.SerializerMethodField()
    def get_specie(self, obj):
        ctx = { 'id':obj.specie.id,
                'name':obj.specie.name,
                'prites':{
                    'back_shiny':obj.specie.sprites.back_shiny,
                    'back_female':obj.specie.sprites.back_female,
                    'front_shiny':obj.specie.sprites.front_shiny,
                    'back_default':obj.specie.sprites.back_default,
                    'front_female':obj.specie.sprites.front_female,
                    'front_default':obj.specie.sprites.front_default,
                    'back_shiny_female':obj.specie.sprites.back_shiny_female,
                    'front_shiny_female':obj.specie.sprites.front_shiny_female,
                }
        }
        return ctx

    class Meta:
        model = PokemonCaptured
        fields = ('id','nick_name','is_party_member','specie')
    def create(self, validated_data):
        return PokemonCaptured.objects.create(**validated_data)


class CapturePosSerializer(serializers.ModelSerializer):
    #specie = serializers.SerializerMethodField()
    # def get_specie(self, obj):
    #     return obj.specie.id
    class Meta:
        model = PokemonCaptured
        fields = ('specie','nick_name','is_party_member',)
    def create(self, validated_data):
        print("DAta en el create")
        print(validated_data)
        return PokemonCaptured.objects.create(**validated_data)
