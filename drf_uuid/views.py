from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CustomerSerializer
from .models import CowrywiseCustomer

class CowrywiseAPI(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            uuid = ""
            serializer.save(uuid=uuid)
            return Response(serializer.data)