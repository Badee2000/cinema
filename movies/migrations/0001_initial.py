# Generated by Django 4.2.11 on 2024-03-26 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('protagonists', models.CharField(max_length=255)),
                ('poster', models.ImageField(upload_to='posters/')),
                ('trailer', models.URLField()),
                ('start_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('coming_up', 'Coming Up'), ('starting', 'Starting'), ('running', 'Running'), ('finished', 'Finished')], default='coming_up', max_length=10)),
                ('ranking', models.IntegerField(default=0)),
            ],
        ),
    ]
