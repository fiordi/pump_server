from pump_app.model_classes.Sale import Sale
from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from django.shortcuts import render
from copy import deepcopy
from collections import Counter
from decimal import *
import datetime, json

"""
ManageSaleHandler Class (Singleton)
"""
class ManageSaleHandler(View):


    """
    It creates a new Sale instance ad associates it to an User

    User => User()

    :return Sale()
    """
    def makeNewSale(self, user):
        sale = Sale().makeNewSale(user)
        return sale





    """
    It adds a list of Packets, each one is defined by a quantity, to a Sale

    sale => Sale()
    packets_sale => List[Packet, quantity]

    :return Sale()
    """
    def addPacketList(self, sale, packets_sale):
        from pump_app.model_classes.ManagePacketHandler import ManagePacketHandler
        from pump_app.model_classes.ManageSubscriptionHandler import ManageSubscriptionHandler
        from pump_app.model_classes.SaleLineItem import SaleLineItem

        subscription = sale.user.subscription

        #prima di aggiungere i pacchetti, elimino tutti i pacchetti eventualmente presenti nella sale
        #per azioni precedenti
        sale.packets.clear()
        SaleLineItem.objects.filter(sale=sale).delete()

        for packet_pk, quantity in packets_sale.iteritems():
            if (subscription and ManageSubscriptionHandler().checkPacketInSubscription(subscription, packet_pk)) or not subscription:
                packet = ManagePacketHandler().getPacket(packet_pk)
                sale.addPacket(packet, quantity)
        sale.getAmount()

        sale.save()
        return sale





    """
    It handles the CRUD of Course redirecting the request to REST FRAMEWORK

    base_name => str

    :return viewsets.ModelViewSet()
    """
    def setSaleInfo(self, base_name):
        from pump_app.REST_classes.SaleViewSet import SaleViewSet
        return SaleViewSet

