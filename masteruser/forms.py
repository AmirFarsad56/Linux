from django import forms
from masteruser.models import MasterUserModel


class MasterUserForm(forms.ModelForm):

    class Meta:
        model = MasterUserModel
        fields = ('phone_number',)


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)


class EmailForm(forms.Form):
    subject = forms.CharField(widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)


class MasterUserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MasterUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False
    class Meta():
        model = MasterUserModel
        fields = ('phone_number','picture')
        widgets = {
            'picture': forms.FileInput(attrs={}),
        }
