from django_filters import rest_framework as filters

from basic_library.models import Clients, Authors, Books, Loans, Genres

LIKE = 'unaccent__icontains'
CONTAINS = 'icontains'
STARTSWITH = 'startswith'
EQUALS = 'exact'
LT = 'lt'
GT = 'gt'
GTE = 'glt'
LTE = 'lte'


class ClientFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr=EQUALS)
    name = filters.CharFilter(field_name='name', lookup_expr=LIKE)
    age = filters.NumberFilter(field_name='age', lookup_expr=GTE)
    cpf = filters.CharFilter(field_name='cpf', lookup_expr=STARTSWITH)
    favourite_genre = filters.CharFilter(field_name='id__name', lookup_expr=LIKE)

    class Meta:
        model = Clients
        fields = ['id', 'name', 'age', 'cpf', 'favourite_genre']


class AuthorFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr=EQUALS)
    name = filters.CharFilter(field_name='name', lookup_expr=LIKE)

    class Meta:
        model = Authors
        fields = ['id', 'name']


class BookFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr=EQUALS)
    title = filters.CharFilter(field_name='title', lookup_expr=LIKE)
    author = filters.CharFilter(field_name='id_author__name', lookup_expr=LIKE)
    genre = filters.CharFilter(field_name='id_genre__name', lookup_expr=LIKE)
    number_pages = filters.NumberFilter(field_name='number_page', lookup_expr=GTE)
    available_copies = filters.NumberFilter(field_name='available_copies', lookup_expr=GTE)

    class Meta:
        model = Books
        fields = ['id', 'title', 'id_author', 'id_genre', 'number_pages', 'available_copies']


class GenreFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr=EQUALS)
    name = filters.CharFilter(field_name='name', lookup_expr=LIKE)

    class Meta:
        model = Genres
        fields = ['id', 'name']

class LoanFilter(filters.FilterSet):
    id = filters.NumberFilter(field_name='id', lookup_expr=EQUALS)
    client = filters.CharFilter(field_name='id_client__name', lookup_expr=LIKE)
    book = filters.CharFilter(field_name='id_book__name', lookup_expr=LIKE)
    loan_day = filters.DateFilter(field_name='loan_day', lookup_expr=GTE)
    return_day = filters.DateFilter(field_name='return_day', lookup_expr=GTE)

    class Meta:
        model = Loans
        fields = ['id', 'id_client', 'id_book', 'loan_day', 'return_day']
