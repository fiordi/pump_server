from django.contrib import admin

from customer.models import StudentCustomer, SeniorCustomer

admin.site.register(StudentCustomer)
admin.site.register(SeniorCustomer)

