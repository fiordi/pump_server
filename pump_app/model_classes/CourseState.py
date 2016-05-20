from django.db import models


"""
CourseState Class (Interface)
"""
class CourseState(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, unique=True, default='Undefined')

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'

"""
CourseActivated Class (Singleton)
"""
class CourseActivated(CourseState):

    def setName(self):
        self.name = "Activated"
        self.save()

"""
CourseDeativated Class (Singleton)
"""
class CourseDeactivated(CourseState):

    def setName(self):
        self.name = "Deactivated"
        self.save()


"""
CourseIncomplete Class (Singleton)
"""
class CourseIncomplete(CourseState):

    def setName(self):
        self.name = "Incomplete"
        self.save()

"""
CourseTrashed Class (Singleton)
"""
class CourseTrashed(CourseState):

    def setName(self):
        self.name = "Trashed"
        self.save()