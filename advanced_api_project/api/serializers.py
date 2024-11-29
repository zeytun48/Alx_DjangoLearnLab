# api/serializers.py
from rest_framework import serializers
from .models import Author, Book

# Author Serializer
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']  # Include any fields you want in the API response

# Book Serializer
class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Nest the Author serializer within Book

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']  # Specify the fields to serialize

