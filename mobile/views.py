from django.shortcuts import render,redirect

from django.views.generic import View
from mobile.models import Mobiles
from mobile.forms import MobileForm,RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.



# ======================CRUD================================
class MobileListView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()

        if "brand" in request.GET:
            brand=request.GET.get("brand")
            qs=qs.filter(brand__iexact=brand)

        if "display" in request.GET:
            display=request.GET.get("display")
            qs=qs.filter(display__iexact=display)

        if "price_lt" in request.GET:
            amount=request.GET.get("price_lt")
            qs=qs.filter(price__lt=amount)

        return render(request,"mobile_list.html",{"data":qs})
    

# localhost:8000/mobiles/{id}
class MobileDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)

        return render(request,"mobile_detail.html",{"data":qs})
    

# 

class MobileDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        messages.success(request,"mobile has been deleted")

        return redirect("mobile-all")



class MobileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MobileForm()

        return render(request,"mobile_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MobileForm(request.POST,files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"mobiles has been created")
            return redirect("mobile-all")
        else:
            messages.error(request,"mobile was not created")
            return render(request,"mobile_add.html",{"form":form})

        

class MobileUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Mobiles.objects.get(id=id)
        form=MobileForm(instance=obj)
        return render(request,"mobile_edit.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Mobiles.objects.get(id=id)
        form=MobileForm(request.POST,instance=obj,files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"mobile has been updated")

            return redirect("mobile-all")
        else:
            messages.error(request,"mobile was not updated")
            return render(request,"mobile_edit.html",{"form":form})




# ============================Authentication =========================================

class SignUpView(View):

    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)

        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)

            messages.success(request,"account has been created")
            return render(request,"register.html",{"form":form})
        
        else:
            messages.error(request,"failed to create account")
            return render(request,"register.html",{"form":form})
        


class SignInView(View):
    
    def get(self,request,*args,**kwargs):
        form=LoginForm()

        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):

        form=LoginForm(request.POST)

        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                # print("valid credential")
                login(request,user_object)
                # print("user is---------------",request.user)
                return redirect("mobile-all")

            return render(request,"login.html",{"form":form})
        

class SignOutView(View):
    
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")



