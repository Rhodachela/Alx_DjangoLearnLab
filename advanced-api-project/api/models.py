from django.db import models

# Create your models here.

#Represents an author with a name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

#Represents a book with a title, publication year, and a foreign key to an author.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
