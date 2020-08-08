from django.shortcuts import render
from homepage.models import Recipe, Author


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "title": " Recipes"})

def recipe(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe.html", {"recipe": my_recipe})

def author(request, author_id):
    author_info = Author.objects.filter(id=author_id).first()
    return render(request, "author.html", {"author": author_info})
