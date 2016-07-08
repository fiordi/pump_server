from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver




from pump_app.model_classes.Customer import StudentCustomer, SeniorCustomer
from pump_app.model_classes.Packet import StandardPacket, CustomPacket
"""
It automatically associates the class_name to type field on each save()
"""
@receiver(pre_save, sender=StudentCustomer)
@receiver(pre_save, sender=SeniorCustomer)
@receiver(pre_save, sender=StandardPacket)
@receiver(pre_save, sender=CustomPacket)
def set_customer_type(sender, instance, *args, **kwargs):
    instance.type = instance.__class__.__name__



from pump_app.model_classes.Course import Course
"""
It automatically associates the current course instance to CourseCatalog on each save()
"""
@receiver(post_save, sender=Course)
def post_save_linkCourseToCourseCatalog(sender, instance, *args, **kwargs):
    from pump_app.model_classes.CourseCatalog import CourseCatalog

    instance.coursecatalog = CourseCatalog.objects.all()[0]





from pump_app.model_classes.Packet import Packet, CustomPacket, StandardPacket
"""
It automatically associates the current packet instance to PacketCatalog on each save()
"""
@receiver(post_save, sender=Packet)
@receiver(post_save, sender=CustomPacket)
@receiver(post_save, sender=StandardPacket)
def post_save_linkPacketToPacketCatalog(sender, instance, *args, **kwargs):
    from pump_app.model_classes.PacketCatalog import PacketCatalog

    instance.packetcatalog = PacketCatalog.objects.all()[0]