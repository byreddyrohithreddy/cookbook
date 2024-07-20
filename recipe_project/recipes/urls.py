from django.urls import path
from .views import list_vegetarian_recipes, get_recipes_by_cuisine, get_most_common_ingredients, add_recipe_with_rating

urlpatterns = [
    path('vegetarian/', list_vegetarian_recipes, name='list_vegetarian_recipes'),
    path('cuisine/<str:cuisine>/', get_recipes_by_cuisine, name='get_recipes_by_cuisine'),
    path('common-ingredients/', get_most_common_ingredients, name='get_most_common_ingredients'),
    path('add-recipe/', add_recipe_with_rating, name='add_recipe_with_rating'),
]
