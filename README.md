====> 1_models

from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models

# Book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    number_of_copies_available = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    
    
    # Ensure number_of_copies_available is always non-negative
    def save(self, *args, **kwargs):
        if self.number_of_copies_available < 0:
            raise ValueError("Number of copies available cannot be negative")
        super().save(*args, **kwargs)


# Users model
class Users(AbstractUser):
    date_of_membership = models.DateField(default=timezone.now)
    active_status = models.BooleanField(default=True)

   
#class Users(models.Model):
   # username = models.CharField(max_length=150, unique=True)
   # email = models.EmailField(unique=True)
   # date_of_membership = models.DateField(auto_now_add=True)
    # active_status = models.BooleanField(default=True)


    def __str__(self):
        return self.username

# Transaction model
class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    check_out_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} borrowed {self.book.title}"

    # Ensure return_date is not set before check_out_date
    def save(self, *args, **kwargs):
        if self.return_date and self.return_date < self.check_out_date:
            raise ValueError("Return date cannot be before check-out date")
        super().save(*args, **kwargs)


# signale give a token automaticlly to user

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


=====> 2_ serializer

from rest_framework import serializers
from .models import Book , Users , Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' 


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__' 


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__' 

=====> 3_veiws

from rest_framework import generics
from .models import Book , Users , Transaction
from .serializers import BookSerializer , UsersSerializer , TransactionSerializer
from rest_framework.authentication import  TokenAuthentication

# 1.1-  List all books and create new book

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]

# 1.2-  Retrieve, update, or delete a specific book

class  BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication]


#2.1- List all  CustomUser and create new book

class UsersListCreateView(generics.ListCreateAPIView):
    queryset =  Users.objects.all()
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


=====> 4_urls


from django.urls import path
from .views import BookListCreateView, BookDetailView , UsersListCreateView , UsersDetailView , TransactionDetailView , TransactionListCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),   # List all books and create new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   # Retrieve, update, or delete specific book
    path('Users/', UsersListCreateView.as_view(), name='Users-list-create'),
    path('Users/<int:pk>/', UsersDetailView.as_view(), name='Users-detail'),
    path('Transaction/', TransactionListCreateView.as_view(), name='Transaction-list-create'),
    path('Transaction/<int:pk>/', TransactionDetailView.as_view(), name='Transaction-detail'),
    # token auth
    path('api-auth',obtain_auth_token)

]    
