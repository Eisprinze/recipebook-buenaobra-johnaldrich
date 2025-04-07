from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import RecipeForm,RecipeIngredientForm,RecipeImageForm,IngredientsForm


@login_required
def recipes_list(request):
    recipes = Recipe.objects.all()

    return render(request, 'ledger/recipes_list.html', {'Recipes_List': recipes})


@login_required
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipeIngredients = RecipeIngredient.objects.filter(recipe=recipe)
    recipeImage = RecipeImage.objects.filter(recipe=recipe)
    return render(request, 'ledger/recipe_info.html', {'Recipe_Ingredients': recipeIngredients,'Recipe_Images': recipeImage})


@login_required
def recipe_add(request):
    form = RecipeForm()
    ingredient_form = RecipeIngredientForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        ingredient_form = RecipeIngredientForm(request.POST)

        if form.is_valid() and ingredient_form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            new_ingredient = ingredient_form.save(commit=False)
            new_ingredient.recipe = recipe
            new_ingredient.save()  
            return redirect('ledger:recipe_detail', pk=recipe.pk)

    return render(request, 'ledger/recipe_add.html', {'form': form, 'ingredient_form': ingredient_form})


@login_required
def recipe_add_ingredients(request):
    form = IngredientsForm()

    if request.method == 'POST':
        form = IngredientsForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ledger:recipe_detail')

    return render(request, 'ledger/recipe_add_ingredients.html', {'form': form})

@login_required
def recipe_image_upload(request,pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeImageForm()

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)

        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect('ledger:recipe_detail', pk=recipe.pk)
        
    return render(request, 'ledger/recipe_image_upload.html', {'form': form, 'recipe': recipe})
