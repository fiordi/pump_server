from django.contrib import admin

from pump_app.models import Course
from pump_app.models import CourseCatalog
from pump_app.models import Packet, StandardPacket, CustomPacket
from pump_app.models import PacketCatalog
from pump_app.models import SingleLesson
from pump_app.models import RepeatedLesson
from pump_app.models import Sale
from pump_app.models import SaleLineItem
from pump_app.models import Subscription
from pump_app.models import StudentCustomer, SeniorCustomer
#from pump_app.models import PacketActivated, PacketDeactivated, PacketIncomplete
#from pump_app.models import Activated
#from pump_app.models import Deactivated
#from pump_app.models import Trashed
#from pump_app.models import Incomplete

admin.site.register(Course)
admin.site.register(CourseCatalog)
admin.site.register(PacketCatalog)
admin.site.register(StandardPacket)
admin.site.register(CustomPacket)
admin.site.register(SingleLesson)
admin.site.register(RepeatedLesson)
admin.site.register(Sale)
admin.site.register(SaleLineItem)
admin.site.register(Subscription)
admin.site.register(StudentCustomer)
admin.site.register(SeniorCustomer)
#admin.site.register(PacketActivated)
#admin.site.register(PacketDeactivated)
#admin.site.register(PacketIncomplete)
#admin.site.register(Trashed)
#admin.site.register(Deactivated)
#admin.site.register(Activated)
#admin.site.register(Incomplete)

