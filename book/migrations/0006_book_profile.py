# Generated by Django 5.0.6 on 2024-08-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_profile_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='profile',
            field=models.ManyToManyField(to='book.profile'),
        ),
    ]