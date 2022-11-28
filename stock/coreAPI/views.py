from django.shortcuts import render
from rest_framework.exceptions import APIException
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
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
        queryset = InsideTransaction.objects.all()
       
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


#Create API

class StockCreateAPIView(CreateAPIView):
    serializer_class = StockCreateSerializer
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=data,context={'request':request})
        if serializer.is_valid():
            stock = serializer.save()
            print(stock)
            return Response({
                'message': "Stock created successful",
                'data': serializer.data
            }, status=200, )
        error_keys = list(serializer.errors.keys())
        if error_keys:
            error_msg = serializer.errors[error_keys[0]]
            return Response({'message': error_msg[0]}, status=400)
        return Response(serializer.errors, status=400)