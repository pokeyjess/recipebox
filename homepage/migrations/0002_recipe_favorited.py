# Generated by Django 3.1 on 2020-09-09 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favorited',
            field=models.ManyToManyField(related_name='favorited', to='homepage.Author'),
        ),
    ]