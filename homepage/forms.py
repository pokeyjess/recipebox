from django import forms
from homepage.models import Author, Recipe


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=100)
    instructions = forms.CharField(widget=forms.Textarea)

class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fiels = [
            'title',
            'description',
            'time_required',
            'instructions'
        ]
        exclude = ['author', 'favorited']

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio"]
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(widget=forms.PasswordInput)
