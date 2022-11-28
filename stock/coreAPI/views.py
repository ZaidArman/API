from django.shortcuts import render
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *


# Stock API
class StockAPI(APIView):
    # permission_classes = (IsAuthenticated, CarOwnerUser)
    def get(self,request, *args, **kwargs):    
        queryset = STOCK.objects.all()[:11]
       
        serializer = StockSerializer(queryset, many=True, context={'request': request})
        if serializer:
            return Response({
                'message':'Stock API Data retrieved successfully',
                'success':'True',
                'data':serializer.data
            },status=200)
        return Response({
            'message':'Data retrieval failed',
            'success':'False',
        },status=400)
        

# Transection API
class TransectionAPI(APIView):
    # permission_classes = (IsAuthenticated, CarOwnerUser)
    def get(self,request, *args, **kwargs):    
        queryset = InsideTransection.objects.all()
       
        serializer = InsideTransectionSerializer(queryset, many=True, context={'request': request})
        if serializer:
            return Response({
                'message':'Transection API Data retrieved successfully',
                'success':'True',
                'data':serializer.data
            },status=200)
        return Response({
            'message':'Transection API Data retrieval failed',
            'success':'False',
        },status=400)
    
    
# Valuation API
class ValuationAPI(APIView):
    # permission_classes = (IsAuthenticated, CarOwnerUser)
    def get(self,request, *args, **kwargs):    
        queryset = Valuation.objects.all()[:11]
        serializer = ValuationSerializer(queryset, many=True, context={'request': request})
        if serializer:
            return Response({
                'message':'Valuation API Data retrieved successfully',
                'success':'True',
                'data':serializer.data
            },status=200)
        return Response({
            'message':'Valuation API Data retrieval failed',
            'success':'False',
        },status=400)


