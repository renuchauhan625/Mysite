from django.shortcuts import render
from rest_framework import viewsets
from . import  models
from . serializers import MovieSerilizer
class  MovieViewset(viewsets.ModelViewSet):
    queryset = models.Moviedata.objects.all()
    serializer_class = MovieSerilizer

class ActionViewSet(viewsets.ModelViewSet):
    queryset=models.Moviedata.objects.filter(typ='action')
    serializer_class = MovieSerilizer
class  ComedyViewSet(viewsets.ModelViewSet):
    queryset = models.Moviedata.objects.filter(typ='comedy')
    serializer_class = MovieSerilizer