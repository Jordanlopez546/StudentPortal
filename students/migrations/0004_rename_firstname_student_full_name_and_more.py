# Generated by Django 4.1.6 on 2023-06-18 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firstname',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='lastname',
        ),
    ]
