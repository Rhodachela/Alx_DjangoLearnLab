from . import views
from django.urls import path

urlpatterns = [
    path('books/', views.list_books, name = "list_books"),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
]