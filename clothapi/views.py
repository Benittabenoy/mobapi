from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from clothapi.serializers import ClotheSerializer
from clothapi.models import clothes

class ClothView(APIView):
    def get(self,request,*args,**kwargs):
        qs=clothes.objects.all()
        serializer=ClotheSerializer(qs,many=True)
        return Response(data=serializer.data)

    def post(self,request,*args,**kwargs):
        serializer=ClotheSerializer(data=request.data)
        if serializer.is_valid():
            clothes.objects.create(**serializer.validated_data)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
class ClothDetailView(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        qs=clothes.objects.get(id=id)
        serializer=ClotheSerializer(qs)
        return Response(data=serializer.data)
