from django.db import models


class CoursePrototype(models.Model):

    def clone(self):
        pass

    class Meta:
		abstract = True
