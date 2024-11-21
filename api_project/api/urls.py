from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token  # Import the token authentication view

# Create a router and register the BookViewSet with it
router = DefaultRouter()
router.register(r'books', BookViewSet)  # Automatically creates routes like /books/, /books/<id>/ etc.

urlpatterns = [
    # URL for the BookList view
    path('books/list/', BookList.as_view(), name='book-list'),  # List view for books

    # Include the router-generated URLs for the BookViewSet
    path('', include(router.urls)),  # This will route the /books/ endpoint and others for CRUD operations
    
    # Token authentication URL - Users can retrieve their token for authenticated access
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token retrieval endpoint
]







































