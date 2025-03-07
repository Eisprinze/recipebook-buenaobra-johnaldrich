from django.urls import path
from .views import recipe_detail,recipes_list

urlpatterns = [
    path('recipes/list', recipes_list,name= 'recipes_list'),
    path('recipe/<int:id>', recipe_detail, name='recipe_detail'),

]

app_name = "ledger"