from sportclub.models import SportClubModel
from django import forms
from django.contrib.gis import forms as Gforms
from leaflet.forms.widgets import LeafletWidget



class SportClubForm(forms.ModelForm):

    class Meta():
        model = SportClubModel
        fields = ('phone_number','address','info','picture','location','sportclub_name','company_phone_number',)
        widgets = {
            'address': forms.Textarea(attrs={'id':'textarea1','class': 'materialize-textarea'}),
            'info': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'location': LeafletWidget(),
        }


class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))


class EmailForm(forms.Form):
    subject = forms.CharField()
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}))


class BankInfoForm(forms.ModelForm):
    class Meta():
        model = SportClubModel
        fields = ('bankaccount_ownername','bankaccount_accountnumber',
                  'bankaccount_cardnumber',
                  'bankaccount_bankname')


class SportClubUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SportClubUpdateForm, self).__init__(*args, **kwargs)
        self.fields['picture'].required = False
    class Meta():
        model = SportClubModel
        fields = ('phone_number','address','info','picture','company_phone_number','sportclub_name')
        widgets = {
            'address': forms.Textarea(attrs={'id':'textarea1','class': 'materialize-textarea'}),
            'info': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'picture': forms.FileInput(attrs={},),
        }


class TermsAndConditionsForm(forms.ModelForm):
    class Meta():
        model = SportClubModel
        fields = ('terms_and_conditions',)
        widgets = {
            'terms_and_conditions': forms.Textarea(attrs={'id':'textarea1','class': 'materialize-textarea'}),
        }
