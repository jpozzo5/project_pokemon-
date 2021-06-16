from rest_framework import viewsets  ,generics
from rest_framework.views import APIView
from PokemonApp.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
  
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
  

  
class PokemonsCapturedRestView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        emp = PokemonCaptured.objects.all()
        emp_serializer = CapturePSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)

class PokemonsListRestView(APIView):
    permission_classes = ()
    def get(self, request):
        emp = Pokemon.objects.all()
        emp_serializer = PokemonSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)


class PokemonsRestView(APIView):
    permission_classes = ()
    def get(self, request, pk):
        pk = self.kwargs['pk']
        emp = Pokemon.objects.get(pk = pk)
        emp_serializer = PokemonSerializer(emp)
        return JsonResponse(emp_serializer.data, safe=False)

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    permission_classes = []
    authentication_classes = []

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
