from django.urls import path, include
from rest_framework import routers

from .views import FilmViewSet, WatchedFilmViewSet


router_v1 = routers.DefaultRouter()

router_v1.register('films', FilmViewSet, basename='films')
router_v1.register('watched', WatchedFilmViewSet, basename='watched_films')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
