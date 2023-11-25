

from django.shortcuts import render
from rest_framework.response import Response
from api.serializer import Userserializer,Cakeserializer,CartSerializer,OrderSerializer,ReviewSerializer
from delight.models import cakes,cakevarients,carts,orders,reviews
from rest_framework.decorators import action

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions

class UserCreationView(APIView):

    def post(self,request,*args,**kwargs):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
        
class CakeView(ModelViewSet):        
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=Cakeserializer
    model=cakes
    queryset=cakes.objects.all() 

    @action(methods=["post"],detail=True)
    def cart_add(self,request,*args,**kwargs):
        cid=kwargs.get("pk")
        varient_obj=cakevarients.objects.get(id=cid)
        user=request.user
        serializer=CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cakevarient=varient_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    @action(methods=["post"],detail=True)
    def place_order(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        varient_obj=cakevarients.objects.get(id=id)
        user=request.user
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cakevarient=varient_obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
        

    @action(methods=["post"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")  
        obj=cakevarients.objects.get(id=id)
        user=request.user
        serializer=ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cakevarient=obj,user=user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.data)

        
        
class CartsView(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer=CartSerializer

    def list(self,request,*args,**kwargs):
        qs=carts.objects.filter(user=request.user)
        serializer=CartSerializer(qs,many=True)
        return Response(data=serializer.data)
    
class OrderView(ViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer=OrderSerializer

    def list(self,request,*args,**kwargs):
        qs=orders.objects.filter(user=request.user)
        serializer=OrderSerializer(qs,many=True)
        return Response(data=serializer.data)  
    

    def destroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        instance=orders.objects.get(id=id)
        if instance.user==request.user:
            instance.delete()
            return Response(data={"msg":"deleted"})
        else:
            return Response(data={"message":"permission denied"})    

        
        
        



