# Django Admin Configuration for Book Model

## Step 1: Register the Book Model in the Admin Interface
In `bookshelf/admin.py`, register the `Book` model to make it manageable from the Django admin interface.

```python
from django.contrib import admin
from .models import Book

admin.site.register(Book)

