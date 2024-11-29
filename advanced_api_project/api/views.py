# api/views.py
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# List all books (GET /books/)
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve a single book (GET /books/<int:pk>/)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create a new book (POST /books/)
# Handled by ListCreateAPIView, which allows both GET and POST
from django.shortcuts import render

# Create your views here.
