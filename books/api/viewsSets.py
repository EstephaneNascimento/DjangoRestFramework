from rest_framework import viewsets
from books.api.serializers import BooksSerializer, BooksSerializerTeste
from books.models import Books

class BooksViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializer
    queryset = Books.objects.all()


class TesteViewSet(viewsets.ModelViewSet):
    serializer_class = BooksSerializerTeste
    queryset = Books.objects.all()