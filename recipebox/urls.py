from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from homepage.views import index, recipe, author, add_recipe, add_author

urlpatterns = [
    path('', index, name="homepage"),
    path('recipe/<int:recipe_id>/', recipe),
    path('author/<int:author_id>/', author),
    path('newrecipe/', add_recipe, name="newrecipe"),
    path('newauthor/', add_author, name="newauthor"),
    path('admin/', admin.site.urls),
]
