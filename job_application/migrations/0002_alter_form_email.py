# Generated by Django 5.0.1 on 2024-01-19 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
