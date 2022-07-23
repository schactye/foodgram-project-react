from os import path

from backend.api.views import IngredientsViewSet, RecipeViewSet, TagsViewSet
from django.urls import include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('tags', TagsViewSet, basename='tags')
router.register('ingredients', IngredientsViewSet, basename='ingredients')
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls)),
]
