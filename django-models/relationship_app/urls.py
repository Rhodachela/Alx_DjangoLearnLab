from . import views
from django.urls import path
from .views import list_books
from .views import CustomLoginView, CustomLogoutView, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books/', views.list_books, name = "list_books"),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]