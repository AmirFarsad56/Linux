from django import forms
from session.models import SessionModel


class DaysForm(forms.Form):
    last_day = forms.CharField(required = False)


class DaysForm_2(forms.Form):
    first_day = forms.CharField(required = True)
    last_day = forms.CharField(required = True)



class TimesForm(forms.Form):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'),required = False)
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required = False)
    stop_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'), required = False)


class PriceForm(forms.Form):
    range_start = forms.CharField()
    range_end = forms.CharField()
    price = forms.IntegerField(required = True)


class SessionDeleteForm(forms.Form):
    range_start = forms.CharField()
    range_end = forms.CharField()

class LastDataSetForm(forms.Form):
    first_day = forms.CharField()
