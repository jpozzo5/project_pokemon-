from rest_framework.views import APIView
from PokemonApp.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import  JsonResponse
from rest_framework import status ,generics,viewsets


class TestRestView(APIView):
    permission_classes = ()
    def get(self, request):
        emp = PokemonCaptured.objects.all()
        emp_serializer = CapturePosSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)


class PokemonsCapturedRestView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        emp = PokemonCaptured.objects.all()
        emp_serializer = CapturePSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)

    def post(self, request, format=None):
        serializer = CapturePosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonsCapturedEditRestView(APIView):
    def put(self, request, pk):
        saved_article = generics.get_object_or_404(PokemonCaptured.objects.all(), pk=pk)
        serializer = CapturePosSerializer(instance=saved_article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
            print(serializer.data)
        #return Response({"success": "Article '{}' updated successfully".format(article_saved)})
        return JsonResponse(serializer.data)

    def delete(self, request, pk):
        p_storage = PokemonCaptured.objects.get(pk = pk)
        if p_storage:
            p_storage.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


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
