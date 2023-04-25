from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Film
from .serializers import FilmSerializer
# Create your views here.
@api_view()
def show_film(request):
    films = Film.objects.all()
    serializer = FilmSerializer(films, many=True)
    return Response({ "code": 200, "message": "Todo salio bien", "data" : serializer.data})