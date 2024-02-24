from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# import from mobile app
from mobile.models import Mobiles

# import from api
from api.serializers import MobileSerializer


# Create your views here.

# crud
# api for creating and listing mobile
# localhost:8000/api/mobiles/

class MobileListCreateView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        serializer=MobileSerializer(qs,many=True)  #deserialization 
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data) #serialization
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
# localhost:8000/api/mobiles/{id}/
    
class MobileDetailUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs)
        return Response(data=serializer.data)
    
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        mobile_object=Mobiles.objects.get(id=id)
        serializer=MobileSerializer(data=request.data,instance=mobile_object)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
   
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        return Response(data={"message":"deleting a mobile"})







