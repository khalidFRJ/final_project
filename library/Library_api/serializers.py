
from rest_framework import serializers
from .models import Book , Users , Transaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' 


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username', 'email', 'date_of_membership', 'is_active']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__' 



