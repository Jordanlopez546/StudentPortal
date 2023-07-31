from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('settings', views.settings, name='settings'),
    path('registered-course', views.registered_course, name='registered_course'),
    path('courseregistration/', views.courseregistration, name='courseregistration'),
    path('courseunregister/', views.courseunregister, name='courseunregister'),
    path('grades/', views.grades, name='grades'),
]
