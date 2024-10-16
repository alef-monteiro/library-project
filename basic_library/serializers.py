from rest_framework import serializers

from basic_library.models import Clients, Authors, Books, Genres, Loans


# O serializers serve para formatar a saída da API

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        exclude = ['created_at']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        exclude = ['created_at']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        exclude = ['created_at']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        exclude = ['created_at']


class LoanSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    id_client = serializers.PrimaryKeyRelatedField(queryset=Clients.objects.all())
    id_book = serializers.PrimaryKeyRelatedField(queryset=Books.objects.all())

    class Meta:
        model = Loans
        exclude = ['created_at']
