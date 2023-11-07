from django.shortcuts import render

# Create your views here.


from django.views.generic import View

from mobile.models import Mobiles

class MobileListView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()

        return render(request,"mobile_list.html",{"data":qs})
    