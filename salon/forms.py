from django import forms
from salon.models import SalonModel, SalonPictureModel

class SalonForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('area','floor_type','locker','is_futsall','is_volleyball',
                  'is_handball','is_football','is_basketball',
                  'drinking_water','parking_area','shower',
                  'changing_room','safe_keeping','air_conditioner',
                  'local_taxi','wifi','ball_rent','spectator_place','buffet')
        widgets = {
            'is_handball': forms.CheckboxInput(attrs={'class': 'red red-text'}),
        }

class SalonPictureForm(forms.ModelForm):

    class Meta():
        model = SalonPictureModel
        fields = ('picture',)


class SalonConfirmForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('is_confirmed',)


class SalonProfitForm(forms.ModelForm):

    class Meta():
        model = SalonModel
        fields = ('profit_percentage',)
