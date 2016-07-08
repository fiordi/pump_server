from pump_app.model_classes.Packet import Packet, StandardPacket, CustomPacket
from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from django.shortcuts import render
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
    It returns a Packet with given pk, if exists

    packet_pk => int

    :return viewsets.ModelViewSet()
    """
    def getPacket(self, packet_pk):
        try:
            packet = Packet.objects.get(pk=packet_pk)
        except:
            packet = None
        return packet



