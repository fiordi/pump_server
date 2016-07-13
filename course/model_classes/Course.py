from course.model_classes.CourseCatalog import CourseCatalog
from course.model_classes.CoursePrototype import CoursePrototype
from course.model_classes.CourseState import CourseState
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
import datetime

"""
Course Class
"""
class Course(models.Model):
    id = models.AutoField(primary_key=True)

    name = models.TextField(null=True, blank=False, default='Undefined')

    description = models.TextField(null=True, blank=False)

    closed = models.BooleanField(null=False, default=False)

    subscrNumber = models.IntegerField(null=False, default=False)

    startDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    endDate = models.DateTimeField(null=True, auto_now=False, auto_now_add=False)

    state = models.ForeignKey(CourseState, null=True, to_field='name', blank=False, related_name='courses')

    coursecatalog = models.ForeignKey(CourseCatalog, null=True, blank=False, on_delete=models.SET_NULL, related_name='courses')


    """
    It creates a new instance of Course and saves it into db
    """
    def makeNewCourse(self):
        self.save()
        return self

    """
    It returns the Object State related to the current Course instance

    :return CourseState()
    """
    def getState(self):
        return self.state

    """
    It sets the arguments of the current Course instance
    """
    def setInfo(self, name, description, closed, startDate, endDate):
        self.name = name
        self.description = description
        self.closed = closed
        self.startDate = startDate
        self.endDate = endDate
        self.confirmed = False
        self.save()

    """
    It saves the current course instance into db
    """
    def saveCourse(self):
        self.save()


    """
    It adds lessons to the current Course instance.

    startDate => dateTime
    endDate => dateTime
    startTime => dateTime
    endTime => dateTime
    frequency => int (deltadays between two repeated lessons)
    weekDayOfLesson => int (ISO value of the days)
    """
    # startDate e endDate sono degli oggetti di tipo datetime
    def addLesson(self, startDate, endDate, startTime, endTime, frequency, weekDayOfLesson):
        from course.model_classes.LessonFactory import LessonFactory
        LessonFactory().createLesson(self, startDate, endDate, startTime, endTime, frequency, weekDayOfLesson)


    """
    It sets the state of the current Course instance to Activated

    """
    def setActivedState(self):
        from course.model_classes.CourseState import ActivatedCourse

        ActivatedCourse.objects.all()[0].setState(self)
        self.save()

    """
    It sets the state of the current Course instance to Deactivated

    """
    def setDeactivedState(self):
        from course.model_classes.CourseState import DeactivatedCourse

        DeactivatedCourse.objects.all()[0].setState(self)
        self.save()


    """
    It sets the state of the current Course instance to Incomplete

    """
    def setIncompleteState(self):
        from course.model_classes.CourseState import IncompleteCourse

        IncompleteCourse.objects.all()[0].setState(self)
        self.save()


    """
    It sets the state of the current Course instance to Incomplete

    """
    def setTrashedState(self):
        from course.model_classes.CourseState import TrashedCourse

        TrashedCourse.objects.all()[0].setState(self)
        self.save()


    """
    It clones the current Course instance with the related objects
    """
    def clone(self):
        from course.model_classes.RepeatedLesson import RepeatedLesson
        from course.model_classes.SingleLesson import SingleLesson
        from course.model_classes.CourseState import IncompleteCourse
        from copy import deepcopy

        courseNotModified = self
        course = deepcopy(courseNotModified)
        course.pk = None

        #setto lo stato del corso duplicato come Incompleto
        Incomplete = IncompleteCourse.objects.all()[0]
        course.setIncompleteState()
        course.save()

        #cerco tutte le repeatedLessons legate al courseNotModified e le duplico sul nuovo course
        repeatedlessonsNotModified = RepeatedLesson.objects.filter(course = courseNotModified)
        repeatedlessons = deepcopy(repeatedlessonsNotModified)
        for repeatedlesson in repeatedlessons:
            #cerco tutte le singleLessons legate alla repeatedLessons e le associo alla repeatedLesson duplicata
            singlelessonsNotModified = SingleLesson.objects.filter(repeatedlesson = repeatedlesson)
            singlelessons = deepcopy(singlelessonsNotModified)

            #la repeatedlesson duplicata va salvata dopo aver recuperato le singlelessons (altrimenti si perde l'associazione)
            #ma prima del salvataggio della singlelesson (altrimenti la singlelesson viene associata al repeatedCourseNotModified)
            repeatedlesson.pk = None
            repeatedlesson.course = course
            repeatedlesson.save()
            for singlelesson in singlelessons:
                singlelesson.pk = None
                singlelesson.repeatedlesson = repeatedlesson
                singlelesson.save()

        #cerco tutte le singleLessons legate direttamente al courseNotModified e le duplico sul nuovo course
        singlelessonsNotModified = SingleLesson.objects.filter(course = courseNotModified)
        singlelessons = deepcopy(singlelessonsNotModified)
        for singlelesson in singlelessons:
                singlelesson.pk = None
                singlelesson.course = course
                singlelesson.save()

        return course



    def __unicode__(self):
        return self.name + '(' + str(self.id) + ')'
