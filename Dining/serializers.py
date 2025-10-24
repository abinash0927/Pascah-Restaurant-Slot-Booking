from rest_framework import serializers
from .models import DiningTable,Customer

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningTable
        fields = ['table_no','status']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name','contact','table']