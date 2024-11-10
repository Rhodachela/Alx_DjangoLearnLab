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
from django.contrib.auth.decorators import user_passes_test


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

# Helper functions to check user roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {'role': 'Admin'})

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html', {'role': 'Librarian'})

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html', {'role': 'Member'})
