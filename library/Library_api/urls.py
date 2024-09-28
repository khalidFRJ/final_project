
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


