# Generated by Django 4.1.6 on 2023-06-22 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_studentprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
