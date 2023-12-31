# Generated by Django 4.2.1 on 2023-06-23 00:17

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0017_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000000)),
                ('dob', models.DateField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('gender', models.CharField(max_length=1000000)),
                ('address', models.CharField(max_length=1000000)),
                ('nickname', models.CharField(max_length=1000000)),
                ('bio', models.TextField()),
                ('profileimg', models.ImageField(default='blank-profile-picture.png', upload_to='student_profile_photo')),
                ('phone_number', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
