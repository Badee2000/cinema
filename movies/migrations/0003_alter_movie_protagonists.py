# Generated by Django 4.2.11 on 2024-03-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_movie_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='protagonists',
            field=models.JSONField(default=list),
        ),
    ]
