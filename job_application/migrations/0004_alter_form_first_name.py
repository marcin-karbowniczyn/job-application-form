# Generated by Django 5.0.1 on 2024-02-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0003_alter_form_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='first_name',
            field=models.CharField(max_length=80),
        ),
    ]
