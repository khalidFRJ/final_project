
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
