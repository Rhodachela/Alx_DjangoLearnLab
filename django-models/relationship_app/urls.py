from . import views
from django.urls import path
from .views import list_books
from .views import CustomLoginView, CustomLogoutView, register
from django.contrib.auth import views as auth_views
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('books/', views.list_books, name = "list_books"),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # URL for the class-based view
    path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]