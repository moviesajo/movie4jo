# Generated by Django 3.2.3 on 2021-05-22 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0002_auto_20210430_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='First_Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.CharField(default='', max_length=16, verbose_name='movie_id')),
                ('genre_id', models.CharField(default='', max_length=16, verbose_name='genre_id')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='register_time')),
                ('update', models.DateTimeField(auto_now_add=True, verbose_name='modify_time')),
            ],
            options={
                'verbose_name': 'First_Genre',
                'verbose_name_plural': 'First_Genre',
                'db_table': 'first_genre',
            },
        ),
    ]
