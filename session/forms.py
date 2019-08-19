from django import forms
from session.models import SessionModel


class DaysForm(forms.Form):
    last_day = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = False)


class DaysForm_2(forms.Form):
    first_day = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    last_day = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)



class TimesForm(forms.Form):
    start_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',attrs={'id':'start_time','type':'text','class':'timepicker'}),required = False)
    duration = forms.TimeField(widget=forms.TimeInput(format='%H:%M',attrs={'id':'duration','class':'timepicker'}), required = False)
    stop_time = forms.TimeField(widget=forms.TimeInput(format='%H:%M',attrs={'id':'stop_time','class':'timepicker'}), required = False)


class PriceForm(forms.Form):
    range_start = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    range_end = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    price = forms.IntegerField(required = True)


class SessionDeleteForm(forms.Form):
    range_start = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    range_end = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)

class LastDataSetForm(forms.Form):
    first_day = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)


class DiscountPercentageForm(forms.Form):
    range_start = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    range_end = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    discount_percentage = forms.IntegerField(widget=forms.TextInput(attrs={'id':'discount_percentage'}),required = True)


class StatusForm(forms.Form):
    range_start = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    range_end = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
