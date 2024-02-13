# Generated by Django 5.0.2 on 2024-02-12 10:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Контент')),
                ('image', models.CharField(max_length=500, verbose_name='URL изображения')),
                ('post_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время публикации')),
            ],
        ),
    ]
