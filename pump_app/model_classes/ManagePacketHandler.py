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
It automatically associates the current packet instance to PacketCatalog on each save()
"""
@receiver(post_save, sender=Packet)
def post_save_handler(sender, instance, *args, **kwargs):
    from pump_app.model_classes.PacketCatalog import PacketCatalog

    instance.packetcatalog = PacketCatalog.objects.all()[0]


