from django.urls import path
from .views import recipe_detail, recipes_list, recipe_add, recipe_image_upload, recipe_add_ingredients

urlpatterns = [
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/add/',recipe_add,name='recipe_add'),
    path('recipe/add/ingredients',recipe_add_ingredients,name='recipe_add_ingredients'),
    path('recipe/<int:pk>/add_image/', recipe_image_upload, name='recipe_image_upload'),
]

app_name = "ledger"
