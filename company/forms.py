from django import forms
from company.models import TermsModel



class TermsForm(forms.ModelForm):
    class Meta():
        model = TermsModel
        fields = ('terms_condition',)
        widgets = {
            'terms_condition': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }
