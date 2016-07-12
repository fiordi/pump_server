from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver



from packet.model_classes.Packet import StandardPacket, CustomPacket
"""
It automatically associates the class_name to type field on each save()
"""
@receiver(pre_save, sender=StandardPacket)
@receiver(pre_save, sender=CustomPacket)
def set_packet_type(sender, instance, *args, **kwargs):
    instance.type = instance.__class__.__name__



from packet.model_classes.Packet import Packet, CustomPacket, StandardPacket
"""
It automatically associates the current packet instance to PacketCatalog on each save()
"""
@receiver(post_save, sender=Packet)
@receiver(post_save, sender=CustomPacket)
@receiver(post_save, sender=StandardPacket)
def post_save_linkPacketToPacketCatalog(sender, instance, *args, **kwargs):
    from packet.model_classes.PacketCatalog import PacketCatalog

    instance.packetcatalog = PacketCatalog.objects.all()[0]