from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator
from sale.model_classes.SaleState import SaleState, CompletedSale
from sale.model_classes.SalePricingStrategy import CompositePricingStrategy
from packet.model_classes.Packet import Packet
from customer.model_classes.Customer import Customer
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
    def makeNewSale(self, User):
        self.user = User.customer
        self.dateTime = datetime.datetime.now()
        self.save()
        return self

    """
    It adds a packet to current Sale instance creating a new SaleLineItem instance

    packet => Packet()
    quantity => integer

    return Sale()
    """
    def addPacket(self, packet, quantity):
        from sale.model_classes.SaleLineItem import SaleLineItem

        salelineitem = SaleLineItem().makeNewSaleLineItem(packet, quantity)
        self.addSaleLineItem(salelineitem)
        self.packets.add(packet)
        self.save()
        return self



    """
    It adds a SaleLineItem to current Sale instance

    SaleLineItem => SaleLineItem()
    """
    def addSaleLineItem(self, SaleLineItem):
        SaleLineItem.sale = self
        SaleLineItem.save()


    """
    It evals the amount of current Sale instance
    """
    def getAmount(self):
        from sale.model_classes.SaleLineItem import SaleLineItem
        from sale.model_classes.SalePricingStrategyFactory import SalePricingStrategyFactory

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
    It sets the state of the current Sale instance to Incomplete

    """
    def setIncompleteState(self):
        from sale.model_classes.SaleState import IncompleteSale

        IncompleteSale.objects.all()[0].setState(self)
        self.save()

    """
    It sets the state of the current Sale instance to Completed

    """
    def setCompleteState(self):
        from sale.model_classes.SaleState import CompletedSale

        CompletedSale.objects.all()[0].setState(self)
        self.save()


    """
    It sets the state of the current Sale instance to Cancelled

    """
    def setCancelledState(self):
        from sale.model_classes.SaleState import CancelledSale

        CancelledSale.objects.all()[0].setState(self)
        self.save()


    def __unicode__(self):
        return str(self.dateTime) + '(' + str(self.id) + ')'
