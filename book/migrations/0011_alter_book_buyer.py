# Generated by Django 5.0.6 on 2024-08-13 14:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0010_alter_book_author_alter_book_buyer_alter_book_cover'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='buyer',
            field=models.ManyToManyField(null=True, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
    ]