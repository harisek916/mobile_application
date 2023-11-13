from django import forms
from mobile.models import Mobiles

class MobileForm(forms.ModelForm):
    class Meta:
        model=Mobiles
        fields="__all__"
        
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control","placeholder":"enter name"}),
            "price":forms.NumberInput(attrs={"class":"form-control","placeholder":"enter price"}),
            "brand":forms.TextInput(attrs={"class":"form-control","placeholder":"enter brand name"}),
            "specs":forms.TextInput(attrs={"class":"form-control","placeholder":"enter specifications"}),
            "display":forms.TextInput(attrs={"class":"form-control","placeholder":"enter display type"}),


        }