# Generated by Django 4.2.2 on 2023-06-06 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='min_level',
            new_name='max_level',
        ),
    ]
