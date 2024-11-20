from rest_framework import generics, viewsets
from bookshelf.models import Book  # Ensure this import is correct based on your Book model
from .serializers import BookSerializer  # Import the serializer you just created

# Existing ListAPIView view
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # This retrieves all Book objects from the database
    serializer_class = BookSerializer  # This tells the view which serializer to use

# New ModelViewSet for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books from the database
    serializer_class = BookSerializer  # Use the BookSerializer to handle requests











