from django import forms
from commonuser.models import CommonUserModel


class CommonUserForm(forms.ModelForm):

    class Meta:
        model = CommonUserModel
        fields = ('phone_number','picture')


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))


class EmailForm(forms.Form):
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))


class CommonUserUpdateForm(forms.ModelForm):
    class Meta():
        model = CommonUserModel
        fields = ('phone_number','picture')
