from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from mobapi.serializers import MobileSerializer,MobileModelSerializer
from mobapi.models import mobiles

class MobileView(APIView):
    def get(self,request,*args,**kwargs):
        qs=mobiles.objects.all()
        serializer=MobileSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=MobileSerializer(data=request.data)
        if serializer.is_valid():
            mobiles.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class MobileDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=mobiles.objects.get(id=id)
        serializer=MobileSerializer(qs)
        return Response(data=serializer.data)


class MobileModelView(APIView):
    def get(self,request,*args,**kwargs):
        qs=mobiles.objects.all()
        serializer=MobileModelSerializer(qs,many=True)
        return Response(data=serializer.data)
    def post(self,request,*args,**kwargs):
        serializer=MobileModelSerializer(data=request.data)
        if serializer.is_valid():
             serializer.save()
             return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class MobileModelDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(qs)
        return Response(data=serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("id")
        mobile=mobiles.objects.get(id=id)
        serializer=MobileModelSerializer(instance=mobile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
             return Response(data=serializer.errors)


