from django.http import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random, string

from .serializers import CustomerSerializer
from .models import CowrywiseCustomer

class CowrywiseAPI(APIView):
    def get(self, request, *args, **kwargs):
        data = {
                "2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f",
                "2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",
                "2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a"
            }
        return Response(data)
        
    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            letters_numbers = string.ascii_lowercase + string.digits
            uuid = ""
            for i in range(32):
                        uuid += random.choice(letters_numbers)
            serializer.save(uuid=uuid)
            return Response(serializer.data)
        return Response(serializer.errors)