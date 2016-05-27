from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from django.shortcuts import render
from copy import deepcopy
import json

"""
ManageCourseHandler Class (Singleton)
"""
class ManageCourseHandler(View):

    """
    It manages the creation of a new Course instance

    request => HttpRequest()
    """
    def makeNewCourse(self, request):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           from pump_app.model_classes.CourseState import CourseIncomplete
           course = Course().createCourse()
           Incomplete = CourseIncomplete.objects.all()[0]
           course.setState(Incomplete)
           coursecatalog = CourseCatalog.objects.get() # to be continued
           coursecatalog.addCourse(course)
           last_id_course_added =\
               Course.objects.latest('id').id
           return HttpResponse(last_id_course_added)





    """
    It handles the creation of Lesson

    request => HttpRequest()

    :return HttpResponse()
    """
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



    """
    It handles the modify of a Course

    request => HttpRequest()

    :return HttpResponse()
    """
    def modifyCourse(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.Course import Course

            courseID = request.GET.get('courseID', '')

            #recupero il corso da modificare e lo duplico
            courseNotModified = Course.objects.get(pk = courseID)
            courseModified = courseNotModified.clone()
            return HttpResponse(courseModified.pk)

