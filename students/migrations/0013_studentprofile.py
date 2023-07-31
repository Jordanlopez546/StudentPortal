# Generated by Django 4.1.6 on 2023-06-22 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0012_delete_studentprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profileimg', models.ImageField(default='blank-profile-picture.png', upload_to='student_profile_photo')),
                ('bio', models.TextField()),
                ('address', models.CharField(max_length=1000000)),
                ('salutation', models.CharField(blank=True, max_length=1000000)),
                ('marital_status', models.CharField(blank=True, max_length=1000000)),
                ('phone_number', models.CharField(max_length=1000000)),
                ('nationality', models.CharField(blank=True, max_length=1000000)),
                ('nickname', models.CharField(blank=True, max_length=100000)),
                ('id_user', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]