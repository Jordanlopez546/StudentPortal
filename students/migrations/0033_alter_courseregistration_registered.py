# Generated by Django 4.2.1 on 2023-06-24 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0032_remove_course_registered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseregistration',
            name='registered',
            field=models.BooleanField(default=False),
        ),
    ]
