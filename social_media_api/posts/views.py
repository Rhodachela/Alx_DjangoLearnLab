from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.pagination import PageNumberPagination
from .models import Post
from django.db.models import Q

class PostPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class PostViewSet(viewsets.ModelViewSet):
    ...
    pagination_class = PostPagination


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    content = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = ['title', 'content']

class PostViewSet(viewsets.ModelViewSet):
    ...
    filterset_class = PostFilter

class FeedView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not permissions.IsAuthenticated.has_permission(permissions.IsAuthenticated(), request, self):
            return Response({'detail': 'Authentication credentials were not provided.'}, status=401)

        following_users = request.user.following.all() 
        user_following = request.user.following.values_list('id', flat=True)
        Post.objects.filter(author__in=following_users).order_by        
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)