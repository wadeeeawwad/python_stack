# Generated by Django 2.2.4 on 2021-05-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninja_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
    ]