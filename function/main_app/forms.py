from django import forms
from .models import Reservation
from .models import HouseKeepingTaskList
from .models import RealtimeClaim
from .models import OfficeCheckOn
from .models import OfficeCheckOut
from .models import CustomerParkingSystem
from .models import EmployeesParkingSystem

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('room_type_grade', 'reservation_online_name', 'reservation_adult_count',
                'reservation_child_count', 'reservation_group',
                'reservation_start_date', 'reservation_end_date',
                'reservation_breakfast_included')
        labels = {  'room_type_grade':'예약 객실 등급',
                    'reservation_online_name':'예약자 성함',
                    'reservation_adult_count':'숙박자 수',
                    'reservation_child_count':'동반 아동 수',
                    'reservation_group':'소속 단체',
                    'reservation_start_date':'체크인 예정일',
                    'reservation_end_date':'체크아웃 예정일',
                    'reservation_breakfast_included':'조식 포함 여부'
        }
        ROOM_CHOICE = (
                 ('Standard Single','스탠다드 싱글'),
                ('RoomTypeInfo object (Standard Double)', '스위트 더블'),
                ('RoomTypeInfo object (Suite Twin)', '스위트 더블'),
                ('RoomTypeInfo object (Suite Double)', '스위트 더블'),
                ('RoomTypeInfo object (Executive Room)', '스위트 더블'),
        )
        widgets = {
            # 'room_type_grade': forms.Select(choices=ROOM_CHOICE),
            'reservation_start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'reservation_end_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
        fields_classes = {
            'room_type_grade':ROOM_CHOICE
        }

class EmTaskAssignForm(forms.ModelForm):
    class Meta:
        model = HouseKeepingTaskList
        fields = [ #'house_keeping_task_start_time', 'house_keeping_task_end_time',
                'room', 'employee',
                ]
        labels = {
            #'house_keeping_task_start_time': '업무 시작시간',
            #'house_keeping_task_end_time': '업무 마감시간',
            'room': '객실 번호',
            'employee': '직원',
            #'extra_note' : '추가 기록사항'
        }
        #widgets = {
         #   'extra_note': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        #}
        
        

class EmployeeattendancecheckonForm(forms.ModelForm):
    class Meta:
        model = OfficeCheckOn
        fields = ['office_check_on_timestamp', 'employee'
                ]
        labels = {
            'office_check_on_timestamp': '출근시간',
            'employee': '직원명'
        }

class EmployeeattendancecheckoutForm(forms.ModelForm):
    class Meta:
        model = OfficeCheckOut
        fields = ['office_check_out_timestamp', 'employee'
                ]
        labels = {
            'office_check_out_timestamp': '퇴근시간',
            'employee': '직원명'
        }


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

class ParkinglotForm(forms.ModelForm):
    class Meta:
        model = CustomerParkingSystem
        fields = [ 'car_plate_number', 'parking_location', 'parking_in_timestamp'
                ]
    class Meta:
        model = EmployeesParkingSystem
        fields = ['employee', 'car_plate_number', 'parking_location', 'parking_in_timestamp'
                ]

class StartTimeForm(forms.ModelForm):
    class Meta:
        model = HouseKeepingTaskList
        fields = ['room', 'house_keeping_task_start_time' ]
        labels = {
            'room':'하우스키핑 업무 호수',
            'house_keeping_task_start_time':'업무 시작 시간'
        }


class EndTimeForm(forms.ModelForm):
    class Meta:
        model = HouseKeepingTaskList
        fields = ['house_keeping_task_end_time'
                    ]

                    