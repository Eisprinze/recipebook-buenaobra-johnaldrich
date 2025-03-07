from django.db import models
from django.urls import reverse
# Create your models here.

class Ingredients(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        reverse('Ingredients', args=[str(self.name)])

class Recipe(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[str(self.id)])  
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=50)
    ingredients = models.ForeignKey(Ingredients,on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {} , {} '.format(self.ingredients,self.quantity,self.recipe)