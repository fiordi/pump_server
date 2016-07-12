from django.contrib import admin

from sale.models import Sale
from sale.models import SaleLineItem


admin.site.register(Sale)
admin.site.register(SaleLineItem)
