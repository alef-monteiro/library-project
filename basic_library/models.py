from django.db import models


# Create your models here.
class ModelBase(models.Model):
    id = models.BigAutoField(
        db_column='id',
        primary_key=True,
        null=False
    )
    activate = models.BooleanField(
        db_column='activate',
        default=False,
        null=False,
    )
    created_at = models.DateTimeField(
        db_column='created_at',
        null=False,
        auto_now=True,
    )
    modified_at = models.DateTimeField(
        db_column='modified_at',
        null=False,
        auto_now_add=True,
    )

    class Meta:
        abstract = True
        managed = True


class Genres(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=70,
    )


class Authors(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=70,
    )


class Books(ModelBase):
    title = models.CharField(
        db_column="title",
        null=False,
        max_length=70,
    )
    id_author = models.ForeignKey(
        Authors,
        db_column="id_author",
        null=False,
        on_delete=models.DO_NOTHING
    )
    id_genre = models.ForeignKey(
        Genres,
        db_column="id_genre",
        null=False,
        on_delete=models.DO_NOTHING
    )
    number_pages = models.IntegerField(
        db_column='number_pages',
        null=False,
    )
    available_copies = models.IntegerField(
        db_column='available_copies',
        null=False,
    )


class Clients(ModelBase):
    name = models.CharField(
        db_column='name',
        null=False,
        max_length=70,
    )
    age = models.IntegerField(
        db_column='age',
        null=False,
    )
    cpf = models.CharField(
        db_column='cpf',
        null=False,
        max_length=12,
    )
    favourite_genre = models.ForeignKey(
        Genres,
        db_column='favourite_genre',
        null=False,
        on_delete=models.DO_NOTHING,
    )


class Loans(ModelBase):
    id = models.BigAutoField(
        primary_key=True,
        db_column='id',
        null=False,
    )
    id_client = models.ForeignKey(
        Clients,
        db_column='id_client',
        null=False,
        on_delete=models.CASCADE,
    )

    id_book = models.ForeignKey(
        Books,
        db_column='id_book',
        null=False,
        on_delete=models.CASCADE,
    )

    loan_day = models.DateField(
        db_column='loan_day',
        null=False,
        auto_now_add=True,
    )

    return_day = models.DateField(
        db_column='return_day',
        null=False,
        auto_now_add=True,
    )
