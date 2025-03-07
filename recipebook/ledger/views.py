from django.shortcuts import render
from django.http import HttpResponse
from .models import Ingredients,Recipe,RecipeIngredient
# Create your views here.

def recipes_list(request):
    recipes = Recipe.objects.all()
    
    return render(request, 'ledger/recipes_list.html', {'Recipes_List':recipes})

def recipe_detail(request,id):
    recipeIngredients = RecipeIngredient.objects.filter(recipe__name__contains="Recipe " + str(id))

    return render(request, 'ledger/recipe_info.html', {'Recipe_Ingredients' : recipeIngredients})


    
