from django.db import models
#from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    #was body...
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()
    #post_date = models.DateTimeField(default=timezone.now)
    
#cascade, if we delete author, we delete all the items associated with that author

    def __str__(self):
        return f"{self.title} - {self.author.name}"

