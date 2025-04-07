from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import *

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class UserAdmin(UserAdmin):
    inlines = [ProfileInline,]


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage
    fields = ('image', 'description')


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeImageInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Ingredients)
admin.site.register(RecipeIngredient)
admin.site.register(RecipeImage)
admin.site.register(Recipe, RecipeAdmin)
