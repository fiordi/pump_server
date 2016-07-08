from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.response import Response
from pump_app.model_classes.Subscription import Subscription
from pump_app.model_classes.Packet import Packet, CustomPacket, StandardPacket
from pump_app.model_classes.SaleLineItem import SaleLineItem
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


    def confirmSale(self, subscription, customer, packets, sale):
        self.setEndDate(subscription, packets, sale)
        self.setEndDate(subscription, packets, sale)
        customer.setSubscription(subscription)
        subscription.addPackets(packets)
        subscription.setStateActive()
        sale.setStateComplete()
        return sale


    def setStartDate(self, subscription, packets, sale):
        startDate = subscription.evalStartDate(packets, sale)
        subscription.startDate = startDate
        subscription.save()




    def setEndDate(self, subscription, packets, sale):
        endDateStandardPacket = subscription.evalEndDateStandardPacket(packets, sale)
        endDateCustomPacket = subscription.evalEndDateCustomPacket(packets, sale)

        subscription.endDate = max(endDateCustomPacket, endDateStandardPacket)
        subscription.save()



    def checkPacketInSubscription(self, subscription, packet_pk):
        packet = Packet.objects.get(pk=packet_pk)
        if packet in subscription.packets.all():
            return True
        else:
            return False




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
