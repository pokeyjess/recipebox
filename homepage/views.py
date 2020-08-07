from django.shortcuts import render
from homepage.models import Recipe


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "title": " Recipes"})

#def post_detail(request, post_id):
    #my_recipe = Recipe.objects.filter(id=post_id).first()
    #return render(request, "recipe.html", {"post": my_recipe})

