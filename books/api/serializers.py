from rest_framework import serializers
from books.models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"    


# Só alguns campos serão apresentados
class BooksSerializerTeste(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ("title","author")   