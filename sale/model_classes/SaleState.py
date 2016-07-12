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
CompletedSale Class (Singleton)
"""
class CompletedSale(SaleState):

    def setName(self):
        self.name = "Completed"
        self.save()

    def setState(self, Sale):
        Sale.state = self


"""
IncompleteSale Class (Singleton)
"""
class IncompleteSale(SaleState):

    def setName(self):
        self.name = "Incomplete"
        self.save()

    def setState(self, Sale):
        Sale.state = self

"""
CancelledSale Class (Singleton)
"""
class CancelledSale(SaleState):

    def setName(self):
        self.name = "Cancelled"
        self.save()

    def setState(self, Sale):
        Sale.state = self