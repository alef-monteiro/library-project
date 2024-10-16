# Generated by Django 5.1.2 on 2024-10-16 11:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_library', '0003_alter_authors_created_at_alter_authors_modified_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loans',
            options={'managed': True},
        ),
        migrations.AddField(
            model_name='loans',
            name='activate',
            field=models.BooleanField(db_column='activate', default=False),
        ),
        migrations.AddField(
            model_name='loans',
            name='created_at',
            field=models.DateTimeField(auto_now=True, db_column='created_at'),
        ),
        migrations.AddField(
            model_name='loans',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, db_column='modified_at', default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
