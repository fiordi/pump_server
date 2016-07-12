from django.contrib.auth.models import User
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from packet.model_classes.Packet import Packet
from subscription.model_classes.SubscriptionState import SubscriptionState, ActiveSubscription
import datetime

"""
Subscription Class
"""
class Subscription(models.Model):
    id = models.AutoField(primary_key=True)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    packets = models.ManyToManyField(Packet , blank=False, related_name='subscriptions')

    state = models.ForeignKey(SubscriptionState, to_field='name', null=True, blank=False, on_delete=models.PROTECT, related_name='subscriptions')

    """
    It creates a new instance of Subscription and saves it into db
    """
    def makeNewSubscription(self):
        self.save()
        return self

        """
    It sets the arguments of the current Subscription instance
    """
    def setInfo(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate
        self.save()


    def evalStartDate(self, packets, sale):
        from packet.model_classes.Packet import StandardPacket, CustomPacket

        standard_packets = StandardPacket.objects.filter(pk__in=packets)
        custom_packets = CustomPacket.objects.filter(pk__in=packets)

        startdate_subscription = sale.dateTime
        if not standard_packets:
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
        from packet.model_classes.Packet import StandardPacket
        from sale.model_classes.SaleLineItem import SaleLineItem

        standard_packets = StandardPacket.objects.filter(pk__in=packets)


        #verifica, tra i diversi pacchetti, quello con il maggiore endDate che coincidera' con la data di scadenza
        #della sottoscrizione
        enddate_standard_subscription = sale.dateTime
        if standard_packets:
            enddate_standard_packets = []

            salelineitems = SaleLineItem.objects.filter(sale=sale, packet=standard_packets)
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
        from packet.model_classes.Packet import CustomPacket

        custom_packets = CustomPacket.objects.filter(pk__in=packets)

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



    def setActiveState(self):
        from subscription.model_classes.SubscriptionState import ActiveSubscription

        ActiveSubscription.objects.all()[0].setState(self)
        self.save()


    def setInactiveState(self):
        from subscription.model_classes.SubscriptionState import InactiveSubscription

        InactiveSubscription.objects.all()[0].setState(self)
        self.save()

    def setExpiredState(self):
        from subscription.model_classes.SubscriptionState import ExpiredSubscription

        ExpiredSubscription.objects.all()[0].setState(self)
        self.save()



    def addPackets(self, packets):
        for packet in packets:
            self.packets.add(packet)
        return self.packets


    def checkPacketInSubscription(self, packet_pk):
        packet = Packet.objects.get(pk=packet_pk)
        if packet in self.packets.all():
            return True
        else:
            return False


    def __unicode__(self):
        return str(self.endDate) + '(' + str(self.id) + ')'
