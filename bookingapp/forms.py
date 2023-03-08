from django import forms


from .models import Booking

class BookingCreateForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_day', 'end_day']
        widgets = {
            'start_day': forms.TextInput(attrs={'type': 'date'}),
            'end_day': forms.TextInput(attrs={'type': 'date'}),
        }