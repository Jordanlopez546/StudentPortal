# Generated by Django 4.2.1 on 2023-06-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0039_grade_the_course_alter_grade_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='day',
            field=models.CharField(default='Monday', max_length=1000000),
        ),
    ]
