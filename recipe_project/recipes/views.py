from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Recipe, Rating
from .serializers import RecipeSerializer
from django.db.models import Count

@api_view(['GET'])
def list_vegetarian_recipes(request):
    recipes = Recipe.objects.filter(vegetarian=True)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_recipes_by_cuisine(request, cuisine):
    recipes = Recipe.objects.filter(cuisine=cuisine)
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_most_common_ingredients(request):
    ingredients = Recipe.objects.values('ingredients').annotate(count=Count('ingredients')).order_by('-count')[:10]
    return Response(ingredients)

@api_view(['POST'])
def add_recipe_with_rating(request):
    data = request.data
    recipe = Recipe.objects.create(
        name=data.get('name'),
        ingredients=data.get('ingredients'),
        instructions=data.get('instructions'),
        cuisine=data.get('cuisine'),
        vegetarian=data.get('vegetarian', False)
    )
    rating_value = data.get('rating')
    if rating_value is not None:
        Rating.objects.create(recipe=recipe, rating=rating_value)
    
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)

