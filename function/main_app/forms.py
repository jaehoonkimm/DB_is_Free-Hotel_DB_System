from django import forms
from .models import Reservation

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