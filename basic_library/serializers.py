from rest_framework import serializers

from basic_library.models import Clients, Authors, Books, Genres


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
    class Meta:
        model = Genres
        fields = ['id', 'name']
