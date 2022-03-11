from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    """Test Api View"""

    def get(self, request, format=None):
        """returns a list of APIVie features"""
        an_apiview = [
            'Uses HTTP mrthods as function (get,post,patch,put,delete)',
            'Is simmilar to a traditional django view',
            'Gives you the most control over your application Logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview })