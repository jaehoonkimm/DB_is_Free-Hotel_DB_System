"""function URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('loginhome/', views.loginhome, name="loginhome"),
    path('signuphome/', views.signuphome, name='signuphome'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('reservation/', views.reservation, name="reservation"),
    path('emtaskassign/', views.em_task_assign, name="em_task_assgin"),
    path('employeeattendance/', views.employee_attendance, name="employee_attendance"),
    path('realtimeclaims/', views.realtime_claims, name="realtime_claims"),
    path('parkinglot/', views.parking_lot, name="parking_lot"),
    path('parkinglot/<int:pid>/', views.parking_lot_detail, name="parking_lot_detail"),
    path('accounts/', include('allauth.urls')),
    path('create_reservation_calendar/', views.create_reservation_calendar, name='create_reservation_calendar'),
    path('delete_reservation_calendar/', views.delete_reservation_calendar, name='delete_reservation_calendar'),
    path('room_status/', views.room_status, name='room_status'), 
    path('mypage/', views.em_mytask, name='em_mytask'), 
    path('employee_status/', views.employee_status, name='employee_status'), 
]

