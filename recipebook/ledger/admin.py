from django.contrib import admin
from .models import Ingredients,Recipe,RecipeIngredient
# Register your models here.

admin.site.register(Ingredients)
admin.site.register(Recipe)
admin.site.register(RecipeIngredient)