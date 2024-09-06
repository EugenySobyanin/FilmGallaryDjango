from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets

from .serializers import FilmSerializer, WatchedFilmListSerializer, WatchedFilmAddSerializer
from films.models import Film, WatchedFilms


class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', )


class WatchedFilmViewSet(viewsets.ModelViewSet):
    queryset = WatchedFilms.objects.all()
    serializer_class = WatchedFilmListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return WatchedFilmListSerializer
        return WatchedFilmAddSerializer

    # def get_queryset(self):
    #     return Film.objects.filter(user=self.request.user)
