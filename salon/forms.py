from django import forms
from salon.models import SalonModel, SalonPictureModel
from django.forms import ValidationError

class SalonForm(forms.ModelForm):

    def clean(self):
        super(SalonForm, self).clean()
        # This method will set the `cleaned_data` attribute

        one = self.cleaned_data.get('more_than_twelve_sessions_discount')
        two = self.cleaned_data.get('six_to_twelve_sessions_discount')
        if one >= 100 or two >= 100:
            raise ValidationError('درصد تخفیف نمیتواند مقداری بیشتر از ۱۰۰ داشته باشد')

    class Meta():
        model = SalonModel
        fields = ('area','floor_type','locker','is_futsall','is_volleyball',
                  'is_handball','is_football','is_basketball',
                  'drinking_water','parking_area','shower',
                  'changing_room','safe_keeping','air_conditioner',
                  'local_taxi','wifi','ball_rent','spectator_place','buffet',
                  'more_than_twelve_sessions_discount','six_to_twelve_sessions_discount')


class SalonPictureForm(forms.ModelForm):

    class Meta():
        model = SalonPictureModel
        fields = ('picture',)



class SalonPictureUpdateForm(forms.ModelForm):

    class Meta():
        model = SalonPictureModel
        fields = ('picture',)
        widgets = {
            'picture': forms.FileInput(attrs={},),
        }


class SalonConfirmForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('is_confirmed',)


class SalonProfitForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('profit_percentage',)
