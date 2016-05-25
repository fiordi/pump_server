from django.db import models

"""
SaleState Class (Interface)
"""
class SaleState(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, unique=True, default='Undefined')

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'

"""
SaleCompleted Class (Singleton)
"""
class SaleCompleted(SaleState):

    def setName(self):
        self.name = "Completed"
        self.save()


"""
SaleIncomplete Class (Singleton)
"""
class SaleIncomplete(SaleState):

    def setName(self):
        self.name = "Incomplete"
        self.save()

"""
SaleCancelled Class (Singleton)
"""
class SaleCancelled(SaleState):

    def setName(self):
        self.name = "Cancelled"
        self.save()