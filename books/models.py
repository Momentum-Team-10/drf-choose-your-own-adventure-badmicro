from django.db import models
from django.contrib.auth.models import AbstractUser
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.

class User(AbstractUser):
    def __str__(self):
        return self.username

    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

class Genre(models.Model):
    genre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"<Genre: {self.genre}>"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()
    publisher = models.CharField(max_length=100, blank=True, default='')
    genre = models.ManyToManyField(to=Genre, related_name="books")

    class Meta:
        ordering = ['title']
        unique_together = ['title', 'author']

    def __str__(self):
        return f"<Book: {self.title}>"

class Featured(models.Model):
    featured = models.ForeignKey(
        Book, related_name='featured_books', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.featured