from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

#The Student Profile Model/Database.
class StudentProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=1000000)
    address = models.CharField(max_length=1000000)
    nickname = models.CharField(max_length=1000000, blank=True)
    bio = models.TextField()
    profileimg = models.ImageField(upload_to='student_profile_photo', default='blank-profile-picture.png')
    phone_number = models.CharField(max_length=1000000)
    salutation = models.CharField(max_length=1000000)
    nationality = models.CharField(max_length=1000000)
    status = models.CharField(max_length=1000000)
    course = models.CharField(max_length=1000000)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.user.username
    



#The Courses Model/Database.
class Course(models.Model):
    code = models.CharField(max_length=1000000)
    course = models.CharField(max_length=100000)
    class_size = models.IntegerField()
    lecturer = models.CharField(max_length=10000000)
    time = models.TimeField()
    venue = models.CharField(max_length=1000000)
    room = models.CharField(max_length=1000000)
    registered_count = models.IntegerField(default=0)
    day = models.CharField(max_length=1000000, default="Monday")
    

    def __str__(self):
        return self.course
    



#The Course Registration Model/Database.
class CourseRegistration(models.Model):
    the_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.user.username} - {self.the_course.course}"
    



#The Grades Model/Database.
class Grade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    the_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    test_score = models.FloatField()
    exam_score = models.FloatField()
    total_score = models.FloatField()
    gpa = models.FloatField()
    grade = models.CharField(max_length=100000)

    def __str__(self):
        return f"{self.student.user.username} - {self.the_course.course}"

