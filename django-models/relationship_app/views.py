from django.shortcuts import render
from.models import Book

# Create your views here.
def list_books(request):
    render(request, "list_books.html", {"books": books})

from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to show details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
