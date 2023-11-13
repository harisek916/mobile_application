from django.shortcuts import render,redirect

from django.views.generic import View
from mobile.models import Mobiles
from mobile.forms import MobileForm
from django.contrib import messages

# Create your views here.
class MobileListView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()

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
        form=MobileForm(request.POST)

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
        form=MobileForm(request.POST,instance=obj)

        if form.is_valid():
            form.save()
            messages.success(request,"mobile has been updated")

            return redirect("mobile-all")
        else:
            messages.error(request,"mobile was not updated")
            return render(request,"mobile_edit.html",{"form":form})
