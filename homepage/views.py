from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from homepage.models import Recipe, Author
from homepage.forms import AddRecipeForm, AddAuthorForm, LoginForm, SignUpForm, RecipeEditForm


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes, "title": " Recipes"})


def recipe(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    is_author = False
    can_favorite = False
    if request.user.is_authenticated:
        request_author = Author.objects.get(user=request.user)
        can_favorite = True
        if my_recipe.author == request_author:
            is_author = True
    
    return render(request, "recipe.html", {
        "recipe": my_recipe,
        "is_author": is_author,
        "can_favorite": can_favorite
        })


def author(request, author_id):
    author_info = Author.objects.filter(id=author_id).first()
    recipe_list = Recipe.objects.filter(author=author_info)
    favorite_list = Recipe.objects.filter(favorited=author_info)
    return render(request, "author.html", {
        "author": author_info,
        "recipes": recipe_list,
        "favorites": favorite_list
    })

@login_required
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                instructions=data.get('instructions'),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})


@login_required
def add_author(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddAuthorForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                new_user = User.objects.create_user(username=data.get(
                    "username"), password=data.get("password"))
                Author.objects.create(name=data.get(
                    'name'), user=new_user, bio=data.get('bio'))
            return HttpResponseRedirect(reverse("homepage"))
        form = AddAuthorForm()
        return render(request, "generic_form.html", {"form": form})

    else:
        return HttpResponseForbidden("Non-staff not allowed")

@login_required
def recipe_edit_view(request, recipe_id):
    edit_recipe = Recipe.objects.get(id=recipe_id)
    if not request.user.is_staff:
        if edit_recipe.author.user != request.user:
            return HttpResponseRedirect(reverse('homepage'))
    if request.method == 'POST':
        form = RecipeEditForm(request.POST, instance=edit_recipe)
        form.save()
        return HttpResponseRedirect('/recipe/{}/'.format(recipe_id))
    
    form = RecipeEditForm(instance=edit_recipe)
    return render(request, 'generic_form.html', {'form': form})

def favorite_view(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    author = Author.objects.get(user=request.user)
    recipe.favorited.add(author)
    recipe.save()
    return HttpResponseRedirect('/author/{}/'.format(author.id))

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))
            if user:
                login(request, user)
                # return HttpResponseRedirect(reverse("homepage"))
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get(
                "username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
