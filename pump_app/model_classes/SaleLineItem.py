from django.db import models
from pump_app.model_classes.Packet import Packet
from pump_app.model_classes.Sale import Sale

"""
SaleLineItems Class
"""
class SaleLineItem(models.Model):
    id = models.AutoField(primary_key=True)

    sale = models.ForeignKey(Sale, blank=True, related_name='saleslineitems')

    packet = models.ForeignKey(Packet, blank=True, related_name='saleslineitems')

    quantity = models.IntegerKey(null=False, blank=False, default=0)


    """
    It gets the subAmount of the Sale considering packet price and its quantity

    :return Decimal()
    """
    def getSubAmount(self):
        subAmount = self.quantity * self.packet.price
        return subAmount