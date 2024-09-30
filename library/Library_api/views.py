
from rest_framework import generics, status
from .models import Book , Users , Transaction
from .serializers import BookSerializer , UsersSerializer , TransactionSerializer
from rest_framework.authentication import  TokenAuthentication 
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .serializers import BookSerializer
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import redirect

# 1.1-  List all books and create new book

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'author', 'isbn']

# 1.2-  Retrieve, update, or delete a specific book

class  BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 



#2.1- List all  CustomUser and create new book

class UsersListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 


#2.2- Retrieve, update, or delete a specific  CustomUser

class UsersDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class =  UsersSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 


#3.1- List all  CustomUser and create new book

class TransactionListCreateView(generics.ListCreateAPIView):
    queryset =  Transaction.objects.all()
    serializer_class = TransactionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 

#3.2- Retrieve, update, or delete a specific  CustomUser

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class =  TransactionSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 


User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {"message": "User registered successfully."},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        return Response(
            {"detail": "Method 'GET' not allowed."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )
    


# library/views.py

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UsersSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            return redirect('/books/')  # or use the URL name of your view
        return response
    

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return redirect('/books/')  # or use the URL name of your view
        return response