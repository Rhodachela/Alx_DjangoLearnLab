from django.shortcuts import render
from django.views import View
from .models import Library
from .models import Book


# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all book entries from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to show library details and list books in that library
from django.views.generic import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
