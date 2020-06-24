from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializer
from rest_framework import viewsets
from profile_api import models

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
        '''crete a hello msg withb name'''
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():

            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({'message' : message})

        else:

            return Response(serializer.errors)

    def put(self, request, pk = None):
        '''updates an object'''
        return(Response({'method' : 'PUT'}))

    def patch(self, request, pk = None):
        '''upddates an object partially '''
        return(Response({'method' : 'PATCH'}))

    def delete(self, request, pk = None ):
        '''deletes an object'''
        return(Response({'method' : 'DELETE'}))


class HelloViewset(viewsets.ViewSet):
    '''test api viewset'''

    serializer_class = serializer.HelloSerializer

    def list(self, request):
        '''lists the api viewset feaature'''
        a_viewset = [
        'uses actions like list, create, retrieve, update, partial_update ',
        'automaatically maps url '
        'Provide more functionallity'
        ]
        return(Response({'message' : 'Hello', 'a_viewset' : a_viewset}))

    def create(self, request):
        ''''''
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f' Hello {name} '
            return(Response({'msg' : msg}))

        else:

            return Response(serializer.errors)

    def retrieve(self, request, pk = None):
        ''''''
        return(Response({'method' : 'GET'}))

    def update(self, request, pk = None):
        ''''''
        return(Response({'method' : 'PUT'}))

    def partial_update(self, request, pk = None):
        ''''''
        return(Response({'method' : 'PATCH'}))

    def destroy(self, request, pk = None):
        ''''''
        return(Response({'method' : 'delete'}))

class UserProfileViewset(viewsets.ModelViewSet):
    ''''''
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
