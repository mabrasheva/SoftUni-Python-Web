# Generated by Django 4.2.2 on 2023-06-06 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_rename_min_level_game_max_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
    ]
