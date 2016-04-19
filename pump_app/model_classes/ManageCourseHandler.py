from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from copy import deepcopy
import json

class ManageCourseHandler(View):

    def makeNewCourse(self, request):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           from pump_app.model_classes.State import Incomplete
           course = Course().createCourse()
           incomplete = Incomplete()
           course.setState(incomplete)
           coursecatalog = CourseCatalog.objects.get() # to be continued
           coursecatalog.addCourse(course)
           last_id_course_added =\
               Course.objects.latest('id').id
           return HttpResponse(last_id_course_added)

    def setCourseInfo(self, base_name):
        from pump_app.REST_classes.CourseViewSet import CourseViewSet
        #if HttpRequest().method == 'GET':
            # print 'ciao'
        return CourseViewSet

    def setSingleLessonInfo(self, base_name):
        from pump_app.REST_classes.SingleLessonViewSet import SingleLessonViewSet
        #if HttpRequest().method == 'GET':
        return SingleLessonViewSet

    def setRepeatedLessonInfo(self, base_name):
        from pump_app.REST_classes.RepeatedLessonViewSet import RepeatedLessonViewSet
        # if HttpRequest().method == 'GET':
        return RepeatedLessonViewSet

    def addLesson(self, request):
        if request.method == 'POST':
            from pump_app.model_classes.Course import Course
            import datetime
            #associo ad una lista i dati in arrivo dalla richiesta POST
            lesson = json.loads(request.body)

            #converto in oggetti datetime le stringhe della richiesta POST
            startDate = datetime.datetime.strptime(lesson['startDate'], "%Y-%m-%d")
            endDate = datetime.datetime.strptime(lesson['endDate'], "%Y-%m-%d")
            startTime = datetime.datetime.strptime(lesson['startTime'], "%H:%M")
            endTime = datetime.datetime.strptime(lesson['endTime'], "%H:%M")
            frequency = int(lesson['frequency'])

            if 'weekDayOfLesson' in lesson.keys():
                weekDayOfLesson = int(lesson['weekDayOfLesson'])
            else:
                weekDayOfLesson = None

            #leggo l'id del corso a cui devono essere associate le lezioni
            idCourse = lesson['idCourse']

            #recupero il corso a cui devono essere associate le lezioni e procedo con l'aggiunta
            course = Course.objects.get(pk=idCourse)
            course.addLesson(startDate, endDate, startTime, endTime, frequency, weekDayOfLesson)
            return HttpResponse(weekDayOfLesson)

    def saveCourse(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.Course import Course
            idCourse = request.GET.get('idCourse', '')
            course = Course.objects.get(pk=idCourse)
            course.saveCourse()

    def activateCourse(self, request, id_course):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           course = Course.objects.get(pk = id_course)
           coursecatalog = CourseCatalog.objects.get()
           coursecatalog.activateCourse(course)
           return HttpResponse(coursecatalog.activatedcourses.count())

    def getCourseState(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.Course import Course

            courseID = request.GET.get('courseID', '')
            course = Course.objects.get(pk = courseID)
            return HttpResponse(course.getState())

    def modifyCourse(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.Course import Course

            courseID = request.GET.get('courseID', '')

            #recupero il corso da modificare e lo duplico
            courseNotModified = Course.objects.get(pk = courseID)
            courseModified = courseNotModified.clone()
            return HttpResponse(courseModified.pk)



    def debug(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.utility.Utility import Utility

            state = Utility().str_to_class("Activated")
            return HttpResponse(str(state))
