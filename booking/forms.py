from django import forms


class NumberForm(forms.Form):
    numbers = forms.IntegerField()
    range_start = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)
    range_end = forms.CharField(widget=forms.TextInput(attrs={'class':'mp-datepicker'}),required = True)    
