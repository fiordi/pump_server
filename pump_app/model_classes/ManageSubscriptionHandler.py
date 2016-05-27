from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.response import Response
from pump_app.model_classes.Subscription import Subscription
from pump_app.model_classes.Packet import Packet
import json

"""
ManageSubscriptionHandler Class (Singleton)
"""
class ManageSubscriptionHandler(View):


    def makeNewSubscription(self):
        subscription = Subscription()
        subscription.save()

        return subscription


    def evalStartDate(self, packets, sale_datetime):
        #verifica, tra i diversi pacchetti, quello con il minore startDate. Se e' maggiore del dateTime della Sale,
        #fa iniziare la subscription da quella data
        startdate_subscription = sale_datetime
        stardate_packets = []
        for packet in packets:
            stardate_packets.append(packet.startDate)

        mindate_packet = stardate_packets[0]
        for startdate_packet in stardate_packets:
            if startdate_packet < mindate_packet:
                mindate_packet = startdate_packet

        if mindate_packet > startdate_subscription:
            startdate_subscription = mindate_packet

        return startdate_subscription

    def evalEndDate(self, packets):
        #verifica, tra i diversi pacchetti, quello con il maggiore endDate che coincidera' con la data di scadenza
        #della sottoscrizione
        enddate_packets = []
        for packet in packets:
            enddate_packets.append(packet.endDate)

        maxdate_packet = enddate_packets[0]
        for enddate_packet in enddate_packets:
            if enddate_packet > maxdate_packet:
                maxdate_packet = enddate_packet

        enddate_subscription = maxdate_packet

        return enddate_subscription





    def checkPacketInSubscription(self, subscription, packet_pk):
        packet = Packet.objects.get(pk=packet_pk)
        if packet in subscription.packets.all():
            return True
        else:
            return False