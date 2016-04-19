from django.db import models
from solo.models import SingletonModel

class State(models.Model):

    def setCourseState(self, Course):
        pass

    class Meta:
		abstract = True



class Activated(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self




class Deactivated(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self





class Incomplete(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()

        Course.state = self







class Trashed(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    verbose_name = models.CharField(max_length=200, null=True, verbose_name="Incomplete")

    def setCourseState(self, Course):
        #la classe SingletonModel non assegna la pk all'oggetto. Le genericForeignKey tuttavia basano il loro funzionamento su di
        #esso, pertanto viene settato manualmente
        self.id = 1
        self.save()
        Course.state = self


