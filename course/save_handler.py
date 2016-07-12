from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver




from course.model_classes.Course import Course
"""
It automatically associates the current course instance to CourseCatalog on each save()
"""
@receiver(post_save, sender=Course)
def post_save_linkCourseToCourseCatalog(sender, instance, *args, **kwargs):
    from course.model_classes.CourseCatalog import CourseCatalog

    instance.coursecatalog = CourseCatalog.objects.all()[0]


