from rest_framework.serializers import *
from rest_framework import serializers
from .exception import *
from .models import *

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = STOCK
        fields = "__all__"


class InsideTransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsideTransaction
        fields = "__all__"

class ValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuation
        fields = "__all__"


class StockCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, error_messages={'required': "name key is required", 'blank': "name key can't be blank"})
    price = serializers.CharField(max_length=5, error_messages={'required': "price key is required", 'blank': "price key can't be blank"})
    def validate(self, attrs):
        name = attrs['name']
        price = attrs['price']
        if not name or name == "":
            raise APIException400({
                'success' : 'False',
                'message' : 'Please provide name'
            })
        if not price or price == "":
            raise APIException400({
                'success' : 'False',
                'message' : 'Please provide price'
            })
        return attrs

    def create(self, validated_data):
        name = validated_data['name']
        price = validated_data['price']

        if 'name' in validated_data:
            name = validated_data['name']
        else:
            name = None
        if 'price' in validated_data:
            price = validated_data['price']
        else:
            price = None
        stock = STOCK.objects.create(name=name, price=price)
        return validated_data
