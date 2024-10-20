from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, TransactionViewSet, UserViewSet  # Import UserViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')
router.register(r'transactions', TransactionViewSet, basename='transaction')
router.register(r'users', UserViewSet)  # Register the UserViewSet

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),  # Ensure this line is included
]
