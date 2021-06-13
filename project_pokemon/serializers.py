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
    #sprites = serializers.StringRelatedField(many=True, read_only=True)
    sprites = SpritesSerializer(many=True, read_only=True)
    stats =  StatsSerializer(many=True)
    types = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Pokemon
        fields = '__all__'
