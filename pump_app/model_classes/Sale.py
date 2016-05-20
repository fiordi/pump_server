from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator
from pump_app.model_classes.Packet import Packet
import datetime
from decimal import *

"""
Sale Class
"""
class Sale(models.Model):
    id = models.AutoField(primary_key=True)

    dateTime = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    amount_prediscount =  models.DecimalField(null=True, default=Decimal('0'), decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0'))])

    amount =  models.DecimalField(null=True, default=Decimal('0'), decimal_places=2, max_digits=12, validators=[MinValueValidator(Decimal('0.01'))])

    packets = models.ManyToManyField(Packet, blank=True, related_name='sales')

    """
    It creates a new instance of Sale and saves it into db
    """
    def makeNewSale(self):
        self.save()
        return self

    def __unicode__(self):
        return str(self.dateTime) + '(' + str(self.id) + ')'
