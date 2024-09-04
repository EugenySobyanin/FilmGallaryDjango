from django.urls import path, include
from rest_framework import routers

from .views import FilmViewSet


router_v1 = routers.DefaultRouter()

router_v1.register('films', FilmViewSet, basename='films')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
