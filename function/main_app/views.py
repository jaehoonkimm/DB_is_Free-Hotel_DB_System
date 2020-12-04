from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import *

from .forms import ReservationForm
from .forms import EmTaskAssignForm
from .forms import RealTimeClaimsForm
from .forms import EmployeeattendanceForm

from django.utils import timezone
now = timezone.localtime()
import re

def home(request):
    reserv_day = Calendar.objects.order_by('day')
    # room_list = RoomList.objects.filter(room_grade='Suite Double').count
    room_list = ReservationCalendar.objects.all().values()
    return render(request, 'index.html', {'reserv_day':reserv_day, 'room_list':room_list})

def room_status(request):
    room_status = RoomList.objects.all()
    return render(request, 'room_status.html', {'room_list':room_status})

def create_reservation_calendar(request):
    all_date = Calendar.objects.all()
    all_room_type = []
    for room_type in RoomTypeInfo.objects.all():
        all_room_type.append(room_type)
    
    for roomType in all_room_type:
        for i in range(len(all_date)):
            day_val = all_date[i]
            ReservationCalendar.objects.create(room_grade = roomType,
                                                reservation_count = RoomList.objects.all().filter(room_grade=roomType).count(),
                                                day = day_val)
    return redirect('home')
def delete_reservation_calendar(request):
    querySet = ReservationCalendar.objects.all()
    querySet.delete()
    return redirect('home')

#예약 관련 기능
def reservation(request):
    reserv_calendar_date = ReservationCalendar.objects.all()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.reservation_regist_timestamp = timezone.now()
            

            start_checker = 0
            for date in reserv_calendar_date:
                day_in_calendar = re.findall('\(([^)]+)', str(date.day))
                if(str(day_in_calendar[0]) == str(reservation.reservation_start_date) and date.room_grade == reservation.room_type_grade):
                    start_checker = 1
                    temp = date.reservation_count
                    if (temp < 1): # 예약 가능한 잔여석이 없을 경우
                        return render(request, 'reservation.html', {'not_empty_rooms':True})
                    date.reservation_count = temp-1
                    
                elif(start_checker == 1 and str(day_in_calendar[0]) != str(reservation.reservation_end_date)):
                    temp = date.reservation_count
                    if (temp < 1): # 예약 가능한 잔여석이 없을 경우
                        return render(request, 'reservation.html', {'not_empty_rooms':True})
                    date.reservation_count = temp-1

                elif(start_checker == 1 and str(day_in_calendar[0]) == str(reservation.reservation_end_date)):
                    temp = date.reservation_count
                    if (temp < 1): # 예약 가능한 잔여석이 없을 경우
                        return render(request, 'reservation.html', {'not_empty_rooms':True})
                    date.reservation_count = temp-1
                    date.save()
                    break
                else:
                    pass
                date.save()
                reservation.save()
            return redirect('home')
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form':form})

#로그인 관련 기능
def loginhome(request):
    return render(request, 'login.html')

def signuphome(request):
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            errormasg = "잘못 입력 되었습니다."
            return render(request, 'login.html', {'errormasg':errormasg})
    else :
        return redirect('login')

def signup(request):
    if request.method == "POST" :
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

#하우스 키핑 - 직원 업무 배정 기능
def em_task_assign(request):
    if request.method == "POST":
        form = EmTaskAssignForm(request.POST)
        if form.is_valid():
            houseKeepingTaskList = form.save(commit=False)
            #house_keeping_task_creation_timestamp = timezone.now()
            houseKeepingTaskList.save()
            return redirect('home')
    else:
        form = EmTaskAssignForm()
    context = {"form": form}
    return render(request, 'em_task_assign.html', context)

#직원 출퇴근 기능
def employee_attendance(request):
    form = EmployeeattendanceForm()
    return render(request, 'employee_attendance.html', {'form':form})

#실시간 고객 요청 - 직원 업무 할당
def realtime_claims(request):
    if request.method == "POST":
        form = RealTimeClaimsForm(request.POST)
        if form.is_valid():
            RealtimeClaim = form.save(commit=False)
            #claim_creation_time = timezone.now()
            RealtimeClaim.save()
            return redirect('home')
    else:
        form = RealTimeClaimsForm()
    context = {"form": form}
    return render(request, 'realtime_claims.html', context)
