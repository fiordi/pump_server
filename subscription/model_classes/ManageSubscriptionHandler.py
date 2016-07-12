from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.response import Response
from subscription.model_classes.Subscription import Subscription
from packet.model_classes.Packet import Packet, CustomPacket, StandardPacket
from sale.model_classes.SaleLineItem import SaleLineItem
import datetime
import json, os

#recupero le proprieta' di sistema
import pump_site.system_settings
system_settings = pump_site.system_settings

"""
ManageSubscriptionHandler Class (Singleton)
"""
class ManageSubscriptionHandler(View):


    def makeNewSubscription(self):
        subscription = Subscription()
        subscription.save()

        return subscription



    def setStartDate(self, subscription, packets, Sale):
        startDate = subscription.evalStartDate(packets, Sale)
        subscription.startDate = startDate
        subscription.save()


    def setEndDate(self, subscription, packets, Sale):
        endDateStandardPacket = subscription.evalEndDateStandardPacket(packets, Sale)
        endDateCustomPacket = subscription.evalEndDateCustomPacket(packets, Sale)

        subscription.endDate = max(endDateCustomPacket, endDateStandardPacket)
        subscription.save()



    def checkPacketInSubscription(self, subscription, packet_pk):
        return subscription.checkPacketInSubscription(packet_pk)

    def addPackets(self, subscription, packets):
        subscription.addPackets(packets)

    def setActiveState(self, subscription):
        subscription.setActiveState()


    def getNotSubscribedPackets(self, subscription):
        packets = Packet.objects.all()

        packets_not_subscribed =[]

        if subscription:
            for packet in packets:
                packet_pk = packet.id
                if self.checkPacketInSubscription(subscription, packet_pk):
                    pass
                else:
                    packets_not_subscribed.append(packet)
                    packet.image = system_settings.relative_path_image_packet + os.path.basename(packet.image.name)
        else:
            packets_not_subscribed = packets

        return packets_not_subscribed
