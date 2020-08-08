from django.contrib import admin
from django.urls import path
from homepage.views import index, recipe, author

urlpatterns = [
    path('', index),
    path('recipe/<int:recipe_id>/', recipe),
    path('author/<int:author_id>/', author),
    path('admin/', admin.site.urls),
]
