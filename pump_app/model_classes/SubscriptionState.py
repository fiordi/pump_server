from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

"""
SubscriptionState Class (Interface)
"""
class SubscriptionState(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, unique=True, default='Undefined')

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'

"""
SubscriptionActive Class (Singleton)
"""
class SubscriptionActive(SubscriptionState):

    def setName(self):
        self.name = "Active"
        self.save()

"""
SubscriptionInactive Class (Singleton)
"""
class SubscriptionInactive(SubscriptionState):

    def setName(self):
        self.name = "Inactive"
        self.save()


"""
SubscriptionIncomplete Class (Singleton)
"""
class SubscriptionIncomplete(SubscriptionState):

    def setName(self):
        self.name = "Incomplete"
        self.save()