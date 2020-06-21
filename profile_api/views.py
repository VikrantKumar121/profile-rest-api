from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    '''Test api View'''

    def get(self, request, format = None):
        '''reaturns a list of api views features'''
        an_apiview = [
        'uses http methods as func',
        'is similar trad. django view',
        'gives modt control over your app logic',
        'is mapped mannualy to the url',
        ]

        return(Response({'message': 'Hello', 'an_apiview' : an_apiview}))
