# Generated by Django 4.1.6 on 2023-06-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_rename_select_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]