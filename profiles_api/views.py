from rest_framework.views import APIView
from rest_framework.response import Response



class HelloApiView(APIView):
    """Test api view"""
    # def get(self, request, *args, **kwargs):
    def get(self, request, formate=None):
        """Return a list of apiview features"""
        an_apiview = [
            'Uses HTTP methods as fuction (get, post , patch, put, delete)',
            'is similar to a traditonal django view',
            'gives you the most control ocer you application logic',
            'is mapped manually urls'
        ]

        return Response({'message':"hellow!", 'ann_apiview':an_apiview})
