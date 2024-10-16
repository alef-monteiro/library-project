from rest_framework import viewsets, permissions
from basic_library import serializers
from basic_library import filters
from basic_library.models import Clients, Authors, Loans, Genres, Books


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = serializers.ClientSerializer
    filterset_class = filters.ClientFilter
    permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = serializers.AuthorSerializer
    filterset_class = filters.AuthorFilter
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = serializers.BookSerializer
    filterset_class = filters.BookFilter
    permission_classes = [permissions.IsAuthenticated]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = serializers.GenreSerializer
    filterset_class = filters.GenreFilter
    permission_classes = [permissions.IsAuthenticated]


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loans.objects.all()
    serializer_class = serializers.LoanSerializer
    filterset_class = filters.LoanFilter
    permission_classes = [permissions.IsAuthenticated]
