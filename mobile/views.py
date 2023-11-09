from django.shortcuts import render,redirect

# Create your views here.


from django.views.generic import View
from mobile.models import Mobiles
from mobile.forms import MobileForm

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

        return redirect("mobile-all")



class MobileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MobileForm()

        return render(request,"mobile_add.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=MobileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("mobile-all")
        else:
            return render(request,"mobile_add.html",{"form":form})