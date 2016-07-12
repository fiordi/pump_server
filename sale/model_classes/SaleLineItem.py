from django.db import models
from packet.model_classes.Packet import Packet
from sale.model_classes.Sale import Sale

"""
SaleLineItems Class
"""
class SaleLineItem(models.Model):
    id = models.AutoField(primary_key=True)

    sale = models.ForeignKey(Sale, null=True, blank=True, related_name='saleslineitems')

    packet = models.ForeignKey(Packet, null=True, blank=True, related_name='saleslineitems')

    quantity = models.IntegerField(null=False, blank=False, default=0)

    """
    It creates a new SaleLineItem instance

    packet => Packet()
    quantity => int

    :return SaleLineItem()
    """
    def makeNewSaleLineItem(self, packet, quantity):
        self.packet = packet
        self.quantity = quantity
        self.save()
        return self



    """
    It gets the subAmount of the Sale considering packet price and its quantity

    :return Decimal()
    """
    def getSubAmount(self):
        subAmount = self.quantity * self.packet.price
        return subAmount