from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.CharField(max_length=80)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    quote = models.CharField(max_length=50, default="Just another cook")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return f"{self.title} - {self.author.name}"
