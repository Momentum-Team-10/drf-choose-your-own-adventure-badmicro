from rest_framework import serializers
from .models import Book, User


class BookSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Book
        fields = ('url', 'title', 'author', 'publication_date',
                    'publisher', 'genre', 'featured', 'owner',)

class UserSerializer(serializers.HyperlinkedModelSerializer):
    books = serializers.HyperlinkedRelatedField(
        many=True, view_name='book-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'books')