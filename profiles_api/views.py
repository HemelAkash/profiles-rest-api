from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers



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
