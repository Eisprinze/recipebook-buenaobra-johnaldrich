from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.


@login_required
def recipes_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'ledger/recipes_list.html', {'Recipes_List': recipes})


@login_required
def recipe_detail(request, recipename):
    recipeIngredients = RecipeIngredient.objects.filter(recipe__name__contains=str(recipename))

    return render(request, 'ledger/recipe_info.html', {'Recipe_Ingredients': recipeIngredients})
