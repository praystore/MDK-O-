from django.contrib import admin
from .models import Category, Topping, Drink, Recipe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Topping)
class ToppingAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'volume_ml', 'created_at')
    list_filter = ('category',)
    search_fields = ('name',)
    filter_horizontal = ('toppings',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('drink',)
    search_fields = ('drink__name',)