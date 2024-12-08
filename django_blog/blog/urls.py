from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, TaggedPostListView
from .views import (
    add_comment, edit_comment, delete_comment
)
from .views import SearchResultsView, PostByTagListView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', delete_comment, name='delete-comment'),
    path('tags/<slug:tag_slug>/', TaggedPostListView.as_view(), name='tagged-posts'),
    path('search/', SearchResultsView.as_view(), name='search-results'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='post-by-tag'),  # URL for displaying posts by tag

]

