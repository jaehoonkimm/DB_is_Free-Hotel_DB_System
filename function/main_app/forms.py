from django import forms
from .models import Reservation
from .models import HouseKeepingTaskList
from .models import RealtimeClaim
from .models import OfficeCheckOn
from .models import OfficeCheckOut

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_online_name', 'reservation_adult_count',
                'reservation_child_count', 'reservation_group',
                'reservation_start_date', 'reservation_end_date',
                'reservation_breakfast_included']
        widgets = {
            'reservation_start_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class EmTaskAssignForm(forms.ModelForm):
    class Meta:
        model = HouseKeepingTaskList
        fields = ['house_keeping_task_id', 'house_keeping_task_start_time', 'house_keeping_task_end_time',
                'room', 'employee', 'house_keeping_task_creation_timestamp'
                ]

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
        fields = [ 'claim_creation_time', 'realtime_clain_content', 'claim_note',
                'check_in', 'employee'
                ]