from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.response import Response
from pump_app.model_classes.Subscription import Subscription
from pump_app.model_classes.Packet import Packet, CustomPacket, StandardPacket
from pump_app.model_classes.SaleLineItem import SaleLineItem
import datetime
import json


"""
ManageSubscriptionHandler Class (Singleton)
"""
class ManageSubscriptionHandler(View):


    def makeNewSubscription(self):
        subscription = Subscription()
        subscription.save()

        return subscription



    def evalStartDate(self, packets, sale):
        standard_packets = StandardPacket.objects.filter(pk__in=packets)
        custom_packets = CustomPacket.objects.filter(pk__in=packets)

        if standard_packets:
            startdate_subscription = sale.dateTime
        else:
            #verifica, tra i diversi pacchetti, quello con il minore startDate. Se e' maggiore del dateTime della Sale,
            #fa iniziare la subscription da quella data
            startdate_subscription = sale.dateTime
            stardate_packets = []
            for custom_packet in custom_packets:
                stardate_packets.append(custom_packet.startDate)

            mindate_packet = stardate_packets[0]
            for startdate_packet in stardate_packets:
                if startdate_packet < mindate_packet:
                    mindate_packet = startdate_packet

            if mindate_packet > startdate_subscription:
                startdate_subscription = mindate_packet

        return startdate_subscription






    def evalEndDateStandardPacket(self, packets, sale):
        standard_packets = StandardPacket.objects.filter(pk=packets)


        #verifica, tra i diversi pacchetti, quello con il maggiore endDate che coincidera' con la data di scadenza
        #della sottoscrizione
        enddate_standard_subscription = sale.dateTime
        if standard_packets:
            enddate_standard_packets = []

            salelineitems = SaleLineItem.objects.filter(sale=sale, packet=StandardPacket.objects.all())
            for salelineitem in salelineitems:
                standard_packet = StandardPacket.objects.get(pk=salelineitem.packet)
                endDate = sale.dateTime + datetime.timedelta(days = salelineitem.quantity * standard_packet.durate )
                enddate_standard_packets.append(endDate)

            maxdate_standard_packet = enddate_standard_packets[0]
            for enddate_standard_packet in enddate_standard_packets:
                if enddate_standard_packet > maxdate_standard_packet:
                    maxdate_standard_packet = enddate_standard_packet

            enddate_standard_subscription = maxdate_standard_packet


        return enddate_standard_subscription




    def evalEndDateCustomPacket(self, packets, sale):
        custom_packets = CustomPacket.objects.filter(pk=packets)

        #verifica, tra i diversi pacchetti, quello con il maggiore endDate che coincidera' con la data di scadenza
        #della sottoscrizione
        enddate_custom_subscription = sale.dateTime
        if custom_packets:
            enddate_custom_packets = []
            for custom_packet in custom_packets:
                enddate_custom_packets.append(custom_packet.endDate)

            maxdate_custom_packet = enddate_custom_packets[0]
            for enddate_custom_packet in enddate_custom_packets:
                if enddate_custom_packet > maxdate_custom_packet:
                    maxdate_custom_packet = enddate_custom_packet

            enddate_custom_subscription = maxdate_custom_packet

        return enddate_custom_subscription




    def checkPacketInSubscription(self, subscription, packet_pk):
        packet = Packet.objects.get(pk=packet_pk)
        if packet in subscription.packets.all():
            return True
        else:
            return False