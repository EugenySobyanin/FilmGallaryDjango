from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import filters
from rest_framework import viewsets

from .serializers import FilmSerializer, WatchedFilmListSerializer, WatchedFilmAddSerializer, PlanFilmListSerializer, PlanFilmAddSerializer
from films.models import Film, WatchedFilms, PlanFilms


User = get_user_model()


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

    def get_queryset(self):
        # return WatchedFilms.objects.filter(user=self.request.user)
        return WatchedFilms.objects.filter(user=User.objects.get(pk=1))

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print('Попали в метод перформ-криэйт.')
        serializer.save(user=User.objects.get(pk=1))


class PlanFilmViewSet(viewsets.ModelViewSet):
    queryset = PlanFilms.objects.all()
    serializer_class = PlanFilmListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return PlanFilmListSerializer
        return PlanFilmAddSerializer

    def get_queryset(self):
        return PlanFilms.objects.filter(user=self.request.user)