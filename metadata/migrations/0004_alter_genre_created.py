# Generated by Django 3.2.3 on 2021-05-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0003_first_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='register_time'),
        ),
    ]