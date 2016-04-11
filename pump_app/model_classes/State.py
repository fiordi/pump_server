from django.db import models

class State(models.Model):

    def setCourseState(self, Course):
        pass

    class Meta:
		abstract = True

