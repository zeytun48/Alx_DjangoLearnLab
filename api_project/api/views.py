# api/views.py
from rest_framework import generics
from bookshelf.models import Book  # Ensure this import is correct based on your Book model
from .serializers import BookSerializer  # Import the serializer you just created

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # This retrieves all Book objects from the database
    serializer_class = BookSerializer  # This tells the view which serializer to use
from django.shortcuts import render

# Create your views here.
