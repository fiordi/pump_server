from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from copy import deepcopy
import json

"""
ManagePacketHandler Class (Singleton)
"""
class ManagePacketHandler(View):

    """
    It handles the CRUD of Course redirecting the request to REST FRAMEWORK

    base_name => str

    :return viewsets.ModelViewSet()
    """
    def setPacketInfo(self, base_name):
        from pump_app.REST_classes.PacketViewSet import PacketViewSet
        return PacketViewSet


    """
    DEBUG METHOD! USE IT CAREFULLY!

    request => HttpRequest()

    :return HttpResponse()
    """
    def debug(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.utility.Utility import Utility

            state = Utility().str_to_class("Activated")
            return HttpResponse(str(state))
