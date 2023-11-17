from django import forms
from mobile.models import Mobiles
from django.contrib.auth.models import User 

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


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
            "password":forms.PasswordInput(attrs={"class":"form-control","type":"password"}),
        }


class LoginForm(forms.Form):
    # attrs={
    #     "type":"password", 
    # }

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # password=forms.CharField(widget=forms.TextInput(attrs=attrs))

