from django.contrib import admin

from packet.models import Packet, StandardPacket, CustomPacket
from packet.models import PacketCatalog


admin.site.register(PacketCatalog)
admin.site.register(StandardPacket)
admin.site.register(CustomPacket)
