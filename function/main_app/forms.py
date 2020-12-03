from django import forms
from .models import Reservation
from .models import HouseKeepingTaskList
from .models import RealtimeClaim
from .models import OfficeCheckOn
from .models import OfficeCheckOut

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room_type_grade', 'reservation_online_name', 'reservation_adult_count',
                'reservation_child_count', 'reservation_group',
                'reservation_start_date', 'reservation_end_date',
                'reservation_breakfast_included']
        labels = {  'room_type_grade':'예약 객실 등급',
                    'reservation_online_name':'예약자 성함',
                    'reservation_adult_count':'숙박자 수',
                    'reservation_child_count':'동반 아동 수',
                    'reservation_group':'소속 단체',
                    'reservation_start_date':'체크인 예정일',
                    'reservation_end_date':'체크아웃 예정일',
                    'reservation_breakfast_included':'조식 포함 여부'
        }
        widgets = {
            'reservation_start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'reservation_end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class EmTaskAssignForm(forms.ModelForm):
    class Meta:
        model = HouseKeepingTaskList
        fields = [ #'house_keeping_task_start_time', 'house_keeping_task_end_time',
                'room', 'employee', 'extra_note'
                ]
        labels = {
            #'house_keeping_task_start_time': '업무 시작시간',
            #'house_keeping_task_end_time': '업무 마감시간',
            'room': '객실 번호',
            'employee': '직원',
            'extra_note' : '추가 기록사항'
        }
        widgets = {
            'extra_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
        

class EmployeeattendanceForm(forms.ModelForm):
    class Meta:
        model = OfficeCheckOn
        fields = ['office_check_on_timestamp', 'employee'
                ]
    class Meta:
        model = OfficeCheckOut
        fields = ['office_check_out_timestamp', 'employee'
                ]

class RealTimeClaimsForm(forms.ModelForm):
    class Meta:
        model = RealtimeClaim
        fields = ['realtime_clain_content', 'claim_note', 'check_in', 
                'employee'
                ]
        widgets = {
            'claim_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'realtime_clain_content': '요청 업무',
            'claim_note': '자세한 요청사항 기입',
            'check_in' : '체크인 번호',
            'employee': '직원'
        }
        #'claim_task_end_time' = forms.DateTimeField(help_text="실시간 고객 요청 받은 시간")
        #renewal_date = forms.DateField(help_text="Enter.")
    