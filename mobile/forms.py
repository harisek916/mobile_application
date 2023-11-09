from django import forms
from mobile.models import Mobiles

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"
        