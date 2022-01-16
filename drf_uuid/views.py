from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random, string

from .serializers import CustomerSerializer
from .models import CowrywiseCustomer

class CowrywiseAPI(APIView):
    """
        An API that uses generic APIView 
    """
    def get(self, request, *args, **kwargs):
        """
            A get emthod that reads both uuid and created_at date field
            as key value pairs
        """
        data = CowrywiseCustomer.objects.filter().values_list('uuid', 'created_at')
        serializer = {}
        for info in data:
            serializer[info[0]] = info[1] 
        if len(serializer) > 1:
            return Response(serializer)
        return {"error" : "No data to display"}
        
    def post(self, request, *args, **kwargs):
        """
            A post method that populates CowrywiseCustomer model 
            with required data/fields as specified in CustomerSerializer
        """
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            letters_numbers = string.ascii_lowercase + string.digits
            uuid = ""
            for i in range(32):
                        uuid += random.choice(letters_numbers)
            serializer.save(uuid=uuid)
            return Response(serializer.data)
        return Response(serializer.errors)