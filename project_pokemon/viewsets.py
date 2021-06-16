from rest_framework import viewsets 
from rest_framework.views import APIView
from PokemonApp.models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.http import  JsonResponse
from rest_framework import status

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
        print(serializer)
        print("voy por**--")
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PokemonsListRestView(APIView):
    permission_classes = ()
    def get(self, request):
        emp = Pokemon.objects.all()
        emp_serializer = PokemonSerializer(emp, many=True)
        return JsonResponse(emp_serializer.data, safe=False)



    # def put(self, request, pk):
    #     saved_article = get_object_or_404(Article.objects.all(), pk=pk)
    #     data = request.data.get('article')
    #     serializer = ArticleSerializer(instance=saved_article, data=data, partial=True
    #     if serializer.is_valid(raise_exception=True):
    #         article_saved = serializer.save()
    #     return Response({"success": "Article '{}' updated successfully".format(article_saved.title)})



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
