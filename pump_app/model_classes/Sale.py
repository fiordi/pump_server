from django.contrib.auth.models import User
from django.db import models
from pump_app.model_classes.Packet import Packet
import datetime

"""
Sale Class
"""
class Sale(models.Model):
    id = models.AutoField(primary_key=True)

    dateTime = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    amount = models.PositiveIntegerField(null=True)

    packets = models.ManyToManyField(Packet, blank=False, related_name='sales')

    """
    It creates a new instance of Sale and saves it into db
    """
    def makeNewSale(self):
        self.save()
        return self

    def __unicode__(self):
        return str(self.dateTime) + '(' + str(self.id) + ')'
