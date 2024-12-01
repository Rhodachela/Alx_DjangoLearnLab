from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

#Serializes the Book model, ensuring the publication year is valid.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

#Serializes the Author model and includes a nested serialization of related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
