from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('basic_library', '0004_alter_loans_options_loans_activate_loans_created_at_and_more'),
    ]

    operations = [
        migrations.RunSQL("CREATE EXTENSION IF NOT EXISTS unaccent;"),
    ]
