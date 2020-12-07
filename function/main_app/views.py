from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from django.contrib import auth
from .models import *

#from django.models import Q

from .forms import ReservationForm
from .forms import EmTaskAssignForm
from .forms import RealTimeClaimsForm
from .forms import EmployeeattendancecheckonForm
from .forms import EmployeeattendancecheckoutForm
from .forms import ParkinglotForm
from .forms import StartTimeForm
from .forms import EndTimeForm

from django.utils import timezone
now = timezone.localtime()
import re

def home(request):
    reserv_day = Calendar.objects.order_by('day')
    # room_list = RoomList.objects.filter(room_grade='Suite Double').count
    room_list = ReservationCalendar.objects.all().values()
    return render(request, 'index.html', {'reserv_day':reserv_day, 'room_list':room_list})

def employee_status(request):
    employee_status = Employees.objects.all()
    housekeeping = HouseKeepingTaskList.objects.all()
    RealtimeClaim_list = RealtimeClaim.objects.all()
    return render(request, 'employee_status.html', {'employee_list':employee_status, 'housekeeping':housekeeping, 'realtimeclaim':RealtimeClaim_list})

def room_status(request):
    room_status = RoomList.objects.all()
    return render(request, 'room_status.html', {'room_list':room_status})

def create_reservation_calendar(request):
    querySet = ReservationCalendar.objects.all()
    querySet.delete()

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
            return redirect('em_task_assgin')
    else:
        form = EmTaskAssignForm()
    context = {"form": form}
    return render(request, 'em_task_assign.html', context)

#직원 출퇴근 기능
def employee_attendance(request):
    if request.method == "POST":
        form1 = EmployeeattendancecheckonForm(request.POST)
        if form1.is_valid():
            OfficeCheckOn = form1.save(commit=False)
            office_check_on_timestamp = timezone.now()
            OfficeCheckOn.save()
            return redirect('employee_attendance')
    elif request.method == "POST":
        form2 = EmployeeattendancecheckoutForm(request.POST)
        if form2.is_valid():
            OfficeCheckOut = form2.save(commit=False)
            OfficeCheckOut.save()
            return redirect('employee_attendance')
    else:
        form1 = EmployeeattendancecheckonForm()
        form2 = EmployeeattendancecheckoutForm()
    context = {"form1": form1, "form2" : form2}
    return render(request, 'employee_attendance.html', context)
    #form1 = EmployeeattendancecheckonForm()
    #form2 = EmployeeattendancecheckoutForm()
    #return render(request, 'employee_attendance.html', {'form1':form1, 'form2':form2})



#실시간 고객 요청 - 직원 업무 할당
def realtime_claims(request):
    if request.method == "POST":
        form = RealTimeClaimsForm(request.POST)
        if form.is_valid():
            RealtimeClaim = form.save(commit=False)
            #claim_creation_time = timezone.now()
            RealtimeClaim.save()
            return redirect('realtime_claims')
    else:
        form = RealTimeClaimsForm()
    context = {"form": form}
    return render(request, 'realtime_claims.html', context)


#주차 예약 기능
def parking_lot(request):
    form1 = EmployeesParkingSystem.objects.order_by('car_plate_number')
    form2 = CustomerParkingSystem.objects.order_by('car_plate_number')
    context = {'form1' : form1, 'form2' : form2}
    return render(request, 'parking_lot.html', context)


#직원 마이페이지 - 업무 불러오기
def em_mytask(request):
    user = request.user
    user = str(user)
    last_name = user[0]
    first_name = user[1:]
    target_employee = Employees.objects.filter(employee_last_name=last_name, employee_first_name=first_name)
    for i in target_employee:
        emp_id = i.employee_id
    
    your_task = HouseKeepingTaskList.objects.filter(employee=emp_id)
    rc_list = RealtimeClaim.objects.filter(employee=emp_id)

    return render(request, 'mypage.html',  {'your_task':your_task, 'rc_list':rc_list, 'last_name':last_name})

#시작시간 기록 
def start_time(request):
    user = request.user
    user = str(user)
    last_name = user[0]
    first_name = user[1:]
    target_employee = Employees.objects.filter(employee_last_name=last_name, employee_first_name=first_name)
    for i in target_employee:
        emp_id = i.employee_id
    your_task = HouseKeepingTaskList.objects.filter(employee=emp_id)
    # rc_list = RealtimeClaim.objects.filter(employee=emp_id)

    time = now
    data = {'Time':time}

    if request.method == "POST":
        form = StartTimeForm(request.POST, data)
        if form.is_valid():
            RealtimeClaim = form.save(commit=False)
            RealtimeClaim.save()
            return redirect('my_page')
    else:
        form = StartTimeForm()
    return render(request, 'start_time.html', {'form': form})

#마감시간 기록
def end_time(request):
    hk_list = HouseKeepingTaskList.objects.all()
    if request.method == "POST":
        form = EndTimeForm(request.POST)
        if form.is_valid():
            RealtimeClaim = form.save(commit=False)
            RealtimeClaim.save()
            return redirect('realtime_claims')
    else:
        form = EndTimeForm()
    return render(request, 'end_time.html', {'form': form})