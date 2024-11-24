from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookList
from rest_framework.authtoken.views import obtain_auth_token


# Create a router instance
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # Register the ViewSet

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    # Include routes managed by the router
    path('', include(router.urls)),  # Auto-generated routes for CRUD operations  # Maps to the BookList view
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token retrieval endpoint
]
