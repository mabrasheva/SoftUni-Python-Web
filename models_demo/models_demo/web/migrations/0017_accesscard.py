# Generated by Django 4.2.1 on 2023-05-07 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_employee_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.employee')),
            ],
        ),
    ]
