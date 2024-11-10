from django.shortcuts import render
from django.views import View
from .models import Library
from .models import Book
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView


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

# User Registration View
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect('home')  # Redirect to homepage or any other view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Login view (uses Django's built-in view)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Logout view (uses Django's built-in view)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
