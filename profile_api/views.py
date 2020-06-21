from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializer

class HelloApiView(APIView):
    '''Test api View'''
    serializer_class = serializer.HelloSerializer

    def get(self, request, format = None):
        '''reaturns a list of api views features'''
        an_apiview = [
        'uses http methods as func',
        'is similar trad. django view',
        'gives modt control over your app logic',
        'is mapped mannualy to the url',
        ]

        return(Response({'message': 'Hello', 'an_apiview' : an_apiview}))

    def post(self, request, format = None):
        ''''''
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message' : message})

        else:

            return Response(serializer.errors)
