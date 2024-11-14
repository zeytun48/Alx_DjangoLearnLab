# Retrieve Operation

**Python Command:**
```python
from bookshelf.models import Book

# Retrieve the Book instance created earlier
book = Book.objects.get(title="1984")

# Print all attributes of the Book instance
print(book.title, book.author, book.publication_year)

