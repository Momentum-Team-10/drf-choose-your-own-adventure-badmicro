from django.shortcuts import render
from rest_framework import generics
from .models import Book, User
from .serializers import BookSerializer
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer