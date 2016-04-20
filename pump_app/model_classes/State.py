from django.db import models
from solo.models import SingletonModel

"""
State Class (Interface)
"""
class State(models.Model):

    def setCourseState(self, Course):
        pass

    class Meta:
		abstract = True


"""
Activated Class (Singleton)
"""
class Activated(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    """
    It sets the current Activated instance to a Course

    Course => Course()
    """
    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self



"""
Deativated Class (Singleton)
"""
class Deactivated(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    """
    It sets the current Activated instance to a Course

    Course => Course()
    """
    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self




"""
Incomplete Class (Singleton)
"""
class Incomplete(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    """
    It sets the current Activated instance to a Course

    Course => Course()
    """
    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self


"""
Trashed Class (Singleton)
"""
class Trashed(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    """
    It sets the current Activated instance to a Course

    Course => Course()
    """
    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()
        Course.state = self


