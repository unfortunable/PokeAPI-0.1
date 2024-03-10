from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import PokemonViewSet

router = DefaultRouter()
router.register("Pokemon", PokemonViewSet)

urlpatterns = [
    path('', include(router.urls))
]