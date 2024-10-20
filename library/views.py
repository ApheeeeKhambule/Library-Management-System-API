from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Book, Transaction
from .serializers import BookSerializer, TransactionSerializer
from django.contrib.auth.models import User
from django.utils import timezone
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False, methods=['get'])
    def available(self, request):
        available_books = Book.objects.filter(copies_available__gt=0)
        serializer = self.get_serializer(available_books, many=True)
        return Response(serializer.data)

class TransactionViewSet(viewsets.ViewSet):
    def list(self, request):
        transactions = Transaction.objects.filter(user=request.user)  # List transactions for the logged-in user
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data) 
        user = request.user
        book_id = request.data.get('book_id')
        book = Book.objects.get(id=book_id)

    def create(self, request):
        user = request.user
        book_id = request.data.get('book_id')
        book = Book.objects.get(id=book_id)     

        if book.copies_available > 0:
            book.copies_available -= 1
            book.save()

            transaction = Transaction.objects.create(user=user, book=book)
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'No copies available'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        transaction = Transaction.objects.get(id=pk, user=request.user)

        if transaction.returned_date:
            return Response({'error': 'Book already returned'}, status=status.HTTP_400_BAD_REQUEST)

        transaction.returned_date = timezone.now()
        transaction.save()

        book = transaction.book
        book.copies_available += 1
        book.save()

        return Response(TransactionSerializer(transaction).data)
    
    def delete(self, request, pk=None):
        try:
            transaction = Transaction.objects.get(id=pk, user=request.user)  # Ensure the user owns the transaction
            book = transaction.book
            book.copies_available += 1  # Restore the available copies
            book.save()

            transaction.delete()  # Delete the transaction
            return Response(status=status.HTTP_204_NO_CONTENT)  # Return 204 No Content
        except Transaction.DoesNotExist:
            return Response({'error': 'Transaction not found'}, status=status.HTTP_404_NOT_FOUND)

