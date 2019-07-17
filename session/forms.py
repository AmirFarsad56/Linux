from django import forms
from session.models import SessionModel


class DaysForm(forms.Form):
    last_day = forms.CharField(required = False)
    saturdays = forms.BooleanField(required = False)
    sundays = forms.BooleanField(required = False)
    mondays = forms.BooleanField(required = False)
    tuesdays = forms.BooleanField(required = False)
    wednesdays = forms.BooleanField(required = False)
    thursdays = forms.BooleanField(required = False)
    fridays = forms.BooleanField(required = False)


class DaysForm_2(forms.Form):
    first_day = forms.CharField(required = True)
    last_day = forms.CharField(required = True)



class TimesForm(forms.Form):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    stop_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))


class PriceForm(forms.Form):
    range_start = forms.CharField()
    range_end = forms.CharField()
    price = forms.IntegerField(required = True)


class SessionDeleteForm(forms.Form):
    range_start = forms.CharField()
    range_end = forms.CharField()
