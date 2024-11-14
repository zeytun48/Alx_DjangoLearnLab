# Delete Operation

**Python Command:**
```python
from bookshelf.models import Book

# Retrieve the Book instance to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the Book instance
book.delete()

# Attempt to retrieve all books
books = Book.objects.all()

# Print all books after deletion
print(books)

