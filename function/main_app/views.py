from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Calendar

from .forms import ReservationForm
from .forms import EmTaskAssignForm

def home(request):
    reserv_day = Calendar.objects.order_by('day')
    return render(request, 'index.html', {'reserv_day':reserv_day})

#예약 관련 기능
def reservation(request):
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

#직원 업무 배정 기능
def em_task_assign(request):
    form = EmTaskAssignForm()
    return render(request, 'em_task_assign.html', {'form':form})