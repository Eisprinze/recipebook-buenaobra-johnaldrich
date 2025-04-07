from django import forms
from .models import Recipe, RecipeIngredient, RecipeImage, Ingredients


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredients', 'quantity']

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']

class IngredientsForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields =  ['name']
