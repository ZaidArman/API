from rest_framework.serializers import *
from rest_framework import serializers
from .models import *

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = STOCK
        fields = "__all__"


class InsideTransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsideTransection
        fields = "__all__"

class ValuationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Valuation
        fields = "__all__"
