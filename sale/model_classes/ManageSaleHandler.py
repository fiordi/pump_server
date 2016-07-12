from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from django.shortcuts import render
from sale.model_classes.Sale import Sale
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
    def makeNewSale(self, User):
        sale = Sale().makeNewSale(User)
        return sale



    def confirmSale(self, customer, sale):
        from subscription.model_classes.ManageSubscriptionHandler import ManageSubscriptionHandler

        #verifica se il cliente ha gia' una subscription oppure ne crea una nuova
        if customer.subscription:
            subscription = customer.subscription
        else:
            subscription = ManageSubscriptionHandler().makeNewSubscription()

        try:
            packets = subscription.packets.all() + sale.packets.all()
        except:
            packets = sale.packets.all()


        ManageSubscriptionHandler().setStartDate(subscription, packets, sale)
        ManageSubscriptionHandler().setEndDate(subscription, packets, sale)
        customer.setSubscription(subscription)
        ManageSubscriptionHandler().addPackets(subscription, packets)
        ManageSubscriptionHandler().setActiveState(subscription)
        sale.setCompleteState()
        return sale



    """
    It adds a list of Packets, each one is defined by a quantity, to a Sale

    sale => Sale()
    packets_sale => List[Packet, quantity]

    :return Sale()
    """
    def addPacketList(self, sale, packets_sale):
        from packet.model_classes.ManagePacketHandler import ManagePacketHandler
        from subscription.model_classes.ManageSubscriptionHandler import ManageSubscriptionHandler
        from sale.model_classes.SaleLineItem import SaleLineItem

        subscription = sale.user.subscription

        #prima di aggiungere i pacchetti, elimino tutti i pacchetti eventualmente presenti nella sale
        #per azioni precedenti
        sale.packets.clear()
        SaleLineItem.objects.filter(sale=sale).delete()

        for packet_pk, quantity in packets_sale.iteritems():
            if not subscription or not ManageSubscriptionHandler().checkPacketInSubscription(subscription, packet_pk):
                packet = ManagePacketHandler().getPacket(packet_pk)
                sale.addPacket(packet, quantity)
        sale.getAmount()

        sale.save()
        return sale


