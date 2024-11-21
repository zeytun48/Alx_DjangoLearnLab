from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated
from bookshelf.models import Book  # Ensure this import is correct based on your Book model
from .serializers import BookSerializer  # Import the serializer you just created

# Existing ListAPIView view with authentication and permissions
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # This retrieves all Book objects from the database
    serializer_class = BookSerializer  # Specify the serializer class
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

# New ModelViewSet for CRUD operations with authentication and permissions
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to handle requests
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

