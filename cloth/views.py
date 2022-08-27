from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from cloth.models import clothes



class ClothsView(APIView):

    def get(self,request,*args,**kwargs):
        return Response({"mobiles":clothes})

    def post(self,request,*args,**kwargs):
        print(request.data)
        qs=request.data
        clothes.append(qs)
        return  Response({"msg":request.data})

class ClothDetailView(APIView):
    def get(self,request,*args,**kwargs):
        print("kwargs",kwargs)
        id=kwargs.get("id")
        id=[cloth for cloth in clothes if cloth.get("id")==id].pop()
        return Response({"data":id})
