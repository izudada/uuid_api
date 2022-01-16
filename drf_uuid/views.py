from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import random, string

from .serializers import CustomerSerializer
from .models import CowrywiseCustomer

class CowrywiseAPI(APIView):
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