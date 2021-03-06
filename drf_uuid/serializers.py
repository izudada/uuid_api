from rest_framework import serializers
from .models import CowrywiseCustomer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CowrywiseCustomer
        fields = ( 'name', 'email', 'age')