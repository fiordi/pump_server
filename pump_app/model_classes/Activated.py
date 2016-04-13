from pump_app.model_classes.State import State
from django.db import models
from solo.models import SingletonModel

class Activated(SingletonModel, State):
    id = models.AutoField(primary_key=True)

    def setCourseState(self, Course):
        Course.state = self
