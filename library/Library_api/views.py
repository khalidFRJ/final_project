
from rest_framework import generics
from .models import Book , Users , Transaction
from .serializers import BookSerializer , UsersSerializer , TransactionSerializer
from rest_framework.authentication import  TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import BookSerializer

# 1.1-  List all books and create new book

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'isbn']

# 1.2-  Retrieve, update, or delete a specific book

class  BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]



#2.1- List all  CustomUser and create new book

class UsersListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [TokenAuthentication]


#2.2- Retrieve, update, or delete a specific  CustomUser

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class =  UsersSerializer
    authentication_classes = [TokenAuthentication]


#3.1- List all  CustomUser and create new book

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset =  Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]

#3.2- Retrieve, update, or delete a specific  CustomUser

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class =  TransactionSerializer
    authentication_classes = [TokenAuthentication]

