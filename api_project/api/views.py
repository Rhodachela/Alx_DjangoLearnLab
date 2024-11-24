from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Retrieve all book records
    serializer_class = BookSerializer  # Use the BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use BookSerializer for serialization