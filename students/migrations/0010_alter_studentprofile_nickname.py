# Generated by Django 4.1.6 on 2023-06-22 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_studentprofile_id_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='nickname',
            field=models.CharField(blank=True, max_length=100000),
        ),
    ]