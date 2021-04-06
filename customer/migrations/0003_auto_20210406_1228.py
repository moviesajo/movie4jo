# Generated by Django 3.1.7 on 2021-04-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='id',
        ),
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='movie/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='rate',
            field=models.CharField(default='', max_length=8, verbose_name='rate'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor',
            field=models.CharField(max_length=128, verbose_name='actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=16, verbose_name='director'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movieId',
            field=models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='movie_id'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movieName',
            field=models.CharField(max_length=16, verbose_name='movie_name'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.CharField(max_length=512, verbose_name='plot'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(max_length=16, verbose_name='year'),
        ),
    ]