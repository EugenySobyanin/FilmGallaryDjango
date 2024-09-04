from django.shortcuts import render
from rest_framework import viewsets

from .serializers import FilmSerializer
from films.models import Film


class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
