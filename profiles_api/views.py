from django.db.models.query import QuerySet
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test api view"""
    # def get(self, request, *args, **kwargs):
    serializer_class = serializers.HelloSerializer

    def get(self, request, formate=None):
        """Return a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as fuction (get, post , patch, put, delete)',
            'is similar to a traditonal django view',
            'gives you the most control ocer you application logic',
            'is mapped manually urls'
        ]

        return Response({'message':"hellow!", 'ann_apiview':an_apiview})
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('username')
            message = f"Hellow {name}"
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({"method":"PUT"})
    
    def patch(self, request, pk=None):
        """Handle partial update an object"""
        return Response({"method":"patch"})
    
    def delete(self, request, pk=None):
        """Handle delete an object"""
        return Response({"method":"delete"})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    serializer_class = serializers.HelloSerializer


    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses action (list, create, retrieve , update, partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code',
        ]
        return Response({'message':'hello', 'a_viewset':a_viewset})

    def create(self, request):
        """Create a new hello message"""

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('username')
            message = f"Hello {name}!"
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )
    def retrieve(self, request, pk=None):
        """Handle geting an object by its ID"""
        return Response({"http_method": 'GET'})
    
    def update(self, request, pk=None):
        """Handle updating an object by its ID"""
        return Response({"http_method": 'update'})
    
    def partial_update(self, request, pk=None):
        """Handle partial updating an object by its ID"""
        return Response({"http_method":'partial update'})
    
    def destroy(self, request, pk=None):
        """Handle destroy an object by its ID"""
        return Response({"http_method":"destroy"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)


