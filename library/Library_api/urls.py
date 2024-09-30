
from django.urls import path , include
from .views import BookListCreateView, BookDetailView , UsersListCreateView , UsersDetailView , TransactionDetailView , TransactionListCreateView
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, CustomTokenObtainPairView 
from .views import RegisterView 



urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),   # List all books and create new book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   # Retrieve, update, or delete specific book
    path('Users/', UsersListCreateView.as_view(), name='Users-list-create'),
    path('Users/<int:pk>/', UsersDetailView.as_view(), name='Users-detail'),
    path('Transaction/', TransactionListCreateView.as_view(), name='Transaction-list-create'),
    path('Transaction/<int:pk>/', TransactionDetailView.as_view(), name='Transaction-detail'),
    # token auth
    path('api-auth',obtain_auth_token),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
   

]    


