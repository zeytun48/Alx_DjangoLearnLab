from rest_framework import generics
from rest_framework.permissions import IsAuthenticated  # Add permission class
from .models import Book
from .serializers import BookSerializer

# List all books (GET /books/)
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

# Retrieve a single book (GET /books/<int:pk>/)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

# Create a new book (POST /books/)
# Handled by ListCreateAPIView, which allows both GET and POST




















