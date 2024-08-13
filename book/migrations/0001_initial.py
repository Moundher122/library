# Generated by Django 5.0.6 on 2024-08-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('stock', models.IntegerField()),
                ('cover', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
