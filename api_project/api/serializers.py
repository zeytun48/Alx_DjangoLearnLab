# api/serializers.py
from rest_framework import serializers
from bookshelf.models import Book  # Adjust the import if necessary

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book  # Replace with your actual Book model
        fields = '__all__'  # This will include all fields of the Book model

