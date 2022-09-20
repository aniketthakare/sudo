from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import customers
from . serializers import customersSerializer

class customerList(APIView):
    def get(self, request):
        customers1=customers.objects.all()
        serializer=customersSerializer(customers1, many=True)
        return Response(serializer.data)
    def post(selfself):
        pass