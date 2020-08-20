from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('recipe/<int:recipe_id>/', views.recipe),
    path('author/<int:author_id>/', views.author),
    path('newrecipe/', views.add_recipe, name="newrecipe"),
    path('newauthor/', views.add_author, name="newauthor"),
    path('login/', views.login_view, name="loginview"),
    path('logout/', views.logout_view, name="logoutview"),
    path('signup/', views.signup_view, name="signupview"),
    path('admin/', admin.site.urls),
]
