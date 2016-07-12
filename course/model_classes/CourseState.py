from django.db import models


"""
CourseState Class (Interface)
"""
class CourseState(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, unique=True, default='Undefined')

    def setName(self):
        pass

    def setState(self):
        pass

    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'

"""
ActivatedCourse Class (Singleton)
"""
class ActivatedCourse(CourseState):

    def setName(self):
        self.name = "Activated"
        self.save()

    def setState(self, Course):
        Course.state = self

"""
CourseDeativated Class (Singleton)
"""
class DeactivatedCourse(CourseState):

    def setName(self):
        self.name = "Deactivated"
        self.save()

    def setState(self, Course):
        Course.state = self

"""
IncompleteCourse Class (Singleton)
"""
class IncompleteCourse(CourseState):

    def setName(self):
        self.name = "Incomplete"
        self.save()

    def setState(self, Course):
        Course.state = self
        self.save()

"""
TrashedCourse Class (Singleton)
"""
class TrashedCourse(CourseState):

    def setName(self):
        self.name = "Trashed"
        self.save()

    def setState(self, Course):
        Course.state = self