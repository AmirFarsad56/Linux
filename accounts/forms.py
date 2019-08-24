from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import UserModel


class UserForm(UserCreationForm):
    '''form for creating a user'''

    terms = forms.BooleanField(
    error_messages={'required': 'You must accept terms and conditions'},
    )

    class Meta(UserCreationForm):
        model = UserModel
        fields = ('username','email','first_name',
                  'last_name','password1','password2')


class TypesForm(forms.Form):
    commonusers = forms.BooleanField(required=False)
    masterusers = forms.BooleanField(required=False)
    sportclubs = forms.BooleanField(required=False)



class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))


class EmailForm(forms.Form):
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))


class UserUpdateForm(forms.ModelForm):
    class Meta():
        model = UserModel
        fields = ('first_name','last_name','email',)


class SuperUserUpdateForm(forms.ModelForm):
    class Meta():
        model = UserModel
        fields = ('first_name','last_name','email','picture')
        widgets = {
            'picture': forms.FileInput(attrs={}),
        }


class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput())
    new_password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(value):
        all_clean_data = super().clean()
        n1 = all_clean_data['new_password']
        n2 = all_clean_data['confirm_password']
        if n1 != n2:
            raise forms.ValidationError("passwords don't match")
