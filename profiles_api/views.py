from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test APIView"""
    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP methods as function(get, post,patch,put,delete)',
        'Is similar to Django view',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})


# Create your views here.
