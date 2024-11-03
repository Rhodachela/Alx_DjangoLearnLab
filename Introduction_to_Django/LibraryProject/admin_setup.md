# Utilizing the Django Admin Interface for Book Management

## Objective
To integrate the Book model with the Django admin interface and customize its display.

## Steps Taken

### 1. Register the Book Model with the Django Admin
- Opened `bookshelf/admin.py`.
- Added the following code:

   ```python
   from django.contrib import admin
   from .models import Book

   @admin.register(Book)
   class BookAdmin(admin.ModelAdmin):
       list_display = ('title', 'author', 'publication_year')
       list_filter = ('author', 'publication_year')
       search_fields = ('title', 'author')