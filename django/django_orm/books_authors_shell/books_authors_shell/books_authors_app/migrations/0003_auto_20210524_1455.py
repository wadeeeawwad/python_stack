# Generated by Django 2.2.4 on 2021-05-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0002_authours_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authours',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books_authors_app.Books'),
        ),
    ]
