# Generated by Django 4.2.1 on 2023-06-25 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0037_remove_grade_the_registered_course_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='the_registered_course',
        ),
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.CharField(max_length=100),
        ),
    ]
