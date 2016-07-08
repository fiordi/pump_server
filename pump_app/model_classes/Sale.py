from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from pump_app.model_classes.SaleState import SaleState, SaleCompleted
from pump_app.model_classes.Packet import Packet
from pump_app.model_classes.Customer import Customer
from pump_app.model_classes.SalePricingStrategy import CompositePricingStrategy
from picklefield.fields import PickledObjectField
import datetime
from decimal import *

"""
Sale Class
"""
class Sale(models.Model):
    id = models.AutoField(primary_key=True)

    dateTime = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    amount_prediscount =  models.DecimalField(null=True, default=Decimal('0'), decimal_places=2, max_digits=7, validators=[MinValueValidator(Decimal('0'))])

    amount =  models.DecimalField(null=True, default=Decimal('0'), decimal_places=2, max_digits=7, validators=[MinValueValidator(Decimal('0'))])

    applied_strategies = PickledObjectField(null=True, blank=True, default= {})

    packets = models.ManyToManyField(Packet, blank=True, related_name='sales')

    state = models.ForeignKey(SaleState, to_field='name', null=True, blank=False, related_name='sales')

    user = models.ForeignKey(Customer, null=True, blank=True, related_name='sales')

    """
    It creates a new instance of Sale and saves it into db
    """
    def makeNewSale(self, user):
        self.user = user.customer
        self.dateTime = datetime.datetime.now()
        self.save()
        return self

    """
    It adds a packet to current Sale instance creating a new SaleLineItem instance
    """
    def addPacket(self, packet, quantity):
        from pump_app.model_classes.SaleLineItem import SaleLineItem

        salelineitem = SaleLineItem().makeNewSaleLineItem(packet, quantity)
        self.addSaleLineItem(salelineitem)
        self.packets.add(packet)
        self.save()
        return self

    """
    It adds a SaleLineItem to current Sale instance
    """
    def addSaleLineItem(self, salelineitem):
        salelineitem.sale = self
        salelineitem.save()


    """
    It evals the amount of current Sale instance
    """
    def getAmount(self):
        from pump_app.model_classes.SaleLineItem import SaleLineItem
        from pump_app.model_classes.SalePricingStrategyFactory import SalePricingStrategyFactory

        self.amount_prediscount = Decimal(0)
        self.applied_strategies = {}

        salelineitems = SaleLineItem.objects.filter(sale=self)
        if salelineitems:
            for salelineitem in salelineitems:
                subamount = salelineitem.getSubAmount()
                self.amount_prediscount = self.amount_prediscount + subamount
        self.amount = self.amount_prediscount

        composite_strategy = SalePricingStrategyFactory().getCompositeBestPricingStrategy()
        composite_strategy.getAmount(self)
        self.save()

        return self.amount


    """
    It sets the state of current Sale instance as complete
    """
    def setStateComplete(self):
        self.state = SaleCompleted.objects.all()[0]
        self.save()
        return self.state


    def __unicode__(self):
        return str(self.dateTime) + '(' + str(self.id) + ')'
