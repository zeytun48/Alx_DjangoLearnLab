# Update Operation

**Python Command:**
```python
from bookshelf.models import Book

# Retrieve the Book instance to update
book = Book.objects.get(title="1984")

# Update the title of the Book
book.title = "Nineteen Eighty-Four"

# Save the changes to the database
book.save()

# Print the updated Book instance
print(book)

