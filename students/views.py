from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User, auth
from django.http import Http404
from django.db.models import Q


#The Home Page, also contains the search panel.
@login_required(login_url='login')
def index(request):
    
    try:
        courses = Course.objects.all()

        context ={
            'courses':courses,
        }
        search_query = request.GET.get('search', '')
        if search_query:
            courses = Course.objects.filter(Q(course__icontains=search_query))
        else:
            courses = Course.objects.all()
    
        course_present = len(courses) > 0

        context = {
            'courses': courses,
            'search_query': search_query,
            'course_present':course_present
        }
        return render(request, 'index.html', context)
    
    except:
        return render(request, 'error.html')



#The Grades Page, To display all the grades, also contains the search panel.
@login_required(login_url='login')
def grades(request):
    search_query = request.GET.get('search', '')
    
    try:
        student_profile = StudentProfile.objects.get(user=request.user)
        if search_query:
            grades = Grade.objects.filter(student=student_profile, the_course__course__icontains=search_query)
        else:
            grades = Grade.objects.filter(student=student_profile)
        
        context = {
            'grades': grades,
            'search_query': search_query,
            'grades_present': len(grades) > 0
        }
        
        return render(request, 'grades.html', context)
    
    except:
        return render(request, 'error.html')



#The Registered Courses Page, To display all the courses registered, also contains the search panel.
@login_required(login_url='login')
def registered_course(request):
    try:
    
        search_query = request.GET.get('search', '')
        student_profile = StudentProfile.objects.get(user=request.user)

        if search_query:
            student_courses = CourseRegistration.objects.filter(student=student_profile, the_course__course__icontains=search_query, registered=True)
        else:
            student_courses = CourseRegistration.objects.filter(student=student_profile, registered=True)

        context = {
            'search_query': search_query,
            'student_courses':student_courses,
            'course_present': len(student_courses) > 0,
        }
        return render(request, 'registered_course.html', context)
    
    except:
        return render(request, 'error.html')



#To register a course.
@login_required(login_url='login')
def courseregistration(request):

    try:
        if request.method == "POST":
            course_id = request.POST.get("course_id")
            student = StudentProfile.objects.get(user=request.user)

            if CourseRegistration.objects.filter(student=student, the_course_id=course_id).exists():
                messages.info(request, 'Course already registered.')
                return redirect('registered_course')
            
            course = Course.objects.get(pk=course_id)

            registration_count = CourseRegistration.objects.filter(student=student).count()
            if registration_count >= 6:
                messages.info(request, "You can only register for a maximum of 6 courses per semester.")
                return redirect('registered_course')

            if course.registered_count < course.class_size:
                registration = CourseRegistration(the_course=course, student=student, registered=True)
                registration.save()
                messages.info(request, 'Course registered.')

            
                course.registered_count += 1
                course.save()

        return redirect('registered_course')
    
    except:
        return render(request, 'error.html')



#To unregister a course.
@login_required(login_url='login') 
def courseunregister(request):
    
    try:
        if request.method == "POST":
            course_id = request.POST.get('course_id')
            student_profile = StudentProfile.objects.get(user=request.user)
            course = Course.objects.get(pk=course_id)

            if CourseRegistration.objects.filter(the_course_id=course_id, student=student_profile).exists():
                unregister = CourseRegistration.objects.get(the_course_id=course_id, student=student_profile)
                unregister.delete()

                course.registered_count -= 1
                course.save()
                messages.info(request, 'Course unregistered successfully.')

            else:
                messages.info(request, 'You did not register for this course.')

        return redirect('registered_course')
    
    except:
        return render(request, 'error.html')



#To Sign Up.
def signup(request):
    
    try:
        if request.method == "POST":
            dob = request.POST['dob']
            gender = request.POST['gender']
            username = request.POST['username']
            email = request.POST['email']
            course = request.POST['course']
            password = request.POST['password']
            password2 = request.POST['password2']

            if password == password2:

                if User.objects.filter(email=email).exists():
                    messages.info(request, "Email already used, Try Another.")
                    return redirect('signup')
            
                elif User.objects.filter(username=username).exists():
                    messages.info(request, "Username already taken, Try Another.")
                    return redirect('signup')
            
                else:
                    new_user = User.objects.create_user(email=email, username=username, password=password)
                    new_user.save()

                    login_user = auth.authenticate(username=username, password=password)
                    auth.login(request, login_user)

                    student_model = User.objects.get(username=username)
                    new_student_profile = StudentProfile.objects.create(
                        user=student_model,
                        id_user=student_model.id,
                        dob=dob,
                        gender=gender,
                        course=course
                    )
                    new_student_profile.save()

                    messages.info(request, f'Welcome {username}.')
                    return redirect('settings')
            
            else:
                messages.info(request, "Password not the same.")
                return redirect('signup')
        else:
            return render(request, 'register.html')
        
    except:
        return render(request, 'error.html')



#To Log In.
def login(request):
    
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
        
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Invalid Credentials.')
                return redirect('login')
        
        else:
            return render(request, 'login.html')
    except:
        return render(request, 'error.html')



#To Log Out.
@login_required(login_url='login')
def logout(request):
    try:
        auth.logout(request)
        return redirect('login')
    except:
        return render(request, 'error.html')



#The Account settings page.
@login_required(login_url='login')
def settings(request):

    try:
        student_profile = StudentProfile.objects.get(user=request.user)

        if request.method == "POST":

            if request.FILES.get('image') == None:
                image = student_profile.profileimg
                bio = request.POST['bio']
                address = request.POST['address']
                phone = request.POST['phone']
                nickname = request.POST['nickname']
                salutation = request.POST['salutation']
                nationality = request.POST['nationality']
                status = request.POST['status']
            
                student_profile.profileimg = image
                student_profile.bio = bio
                student_profile.address = address
                student_profile.phone_number = phone
                student_profile.nickname = nickname
                student_profile.salutation = salutation
                student_profile.nationality = nationality
                student_profile.status = status
                student_profile.save()

            if request.FILES.get('image') != None:
                image = request.FILES.get('image')
                bio = request.POST['bio']
                address = request.POST['address']
                phone = request.POST['phone']
                nickname = request.POST['nickname']
                salutation = request.POST['salutation']
                nationality = request.POST['nationality']
                status = request.POST['status']
            
                student_profile.profileimg = image
                student_profile.bio = bio
                student_profile.address = address
                student_profile.phone_number = phone
                student_profile.nickname = nickname
                student_profile.salutation = salutation
                student_profile.nationality = nationality
                student_profile.status = status
                student_profile.save()

            messages.info(request, 'Profile Saved.')
            return redirect('index')

        else:
            return render(request, 'settings.html', {'student_profile':student_profile})
    
    except:
        return render(request, 'error.html')

    



