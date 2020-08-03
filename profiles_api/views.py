from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers, models, permissions
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    """Test APIView"""

    def get(self, request, format=None):
        an_apiview = [
        'Uses HTTP methods as function(get, post,patch,put,delete)',
        'Is similar to Django view',
        'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({'method':'PUT'})

    def patch(self, request, pk=None):
        return Response({'method':'PATCH'})

    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer


    """Test API ViewSet"""
    def list(self, request):
        """ Return a hello message"""
        a_viewset = [
        'Uses actions (list,create,retrieve,update,partial update)',
        'Automatically maps URLs to routers',
        'Provides more functionality with less code'

        ]
        return Response({'message':'Hello','a_viewset':a_viewset})

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)







# Create your views here.
