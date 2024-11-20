from django.urls import path, include
from rest_framework.routers import DefaultRouter  # Import DefaultRouter
from .views import BookList, BookViewSet  # Import both the ListAPIView and the new BookViewSet

# Create the router instance
router = DefaultRouter()
# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing route for the BookList view (optional, you can remove this if not needed)
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # This includes all routes registered with the router
]








