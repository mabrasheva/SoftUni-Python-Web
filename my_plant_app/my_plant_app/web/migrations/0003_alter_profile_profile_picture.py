# Generated by Django 4.2.1 on 2023-06-03 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.URLField(blank=True, null=True, verbose_name='Profile Picture'),
        ),
    ]
