from django.db import models

"""
CoursePrototype Class (Interface)
"""
class CoursePrototype(models.Model):

    def clone(self):
        pass

    class Meta:
		abstract = True
