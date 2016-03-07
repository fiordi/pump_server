from django.http import HttpResponse, Http404, HttpRequest
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ManageCourseHandler(View):

    def makeNewCourse(self, request):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           course = Course().createCourse(open = False)
           coursecatalog = CourseCatalog.objects.get() # to be continued
           coursecatalog.addCourse(course)
           return HttpResponse('ciao')

    def setCourseInfo(self, base_name):
        from pump_app.REST_classes.CourseViewSet import CourseViewSet
        #if HttpRequest().method == 'GET':
            # print 'ciao'
        return CourseViewSet

    def addLesson(self, request):
        if request.method == 'GET':
            from pump_app.model_classes.Course import Course
            import datetime
            startDate = datetime.datetime.strptime(request.GET.get('startDate', ''), "%d %b %y")
            endDate = datetime.datetime.strptime(request.GET.get('endDate', ''), "%d %b %y")
            startTime = datetime.datetime.strptime(request.GET.get('startTime', ''), "%H:%M")
            endTime = datetime.datetime.strptime(request.GET.get('endTime', ''), "%H:%M")
            frequency = int(request.GET.get('frequency', ''))
            course = Course.objects.get(pk=14)
            course.addLesson(startDate, endDate, startTime, endTime, frequency)
            return HttpResponse(str(startDate) + str(endDate) + str(startTime) + str(endTime))

    def saveCourse(self):
        pass

    def activateCourse(self, request, id_course):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           course = Course.objects.get(pk = id_course)
           coursecatalog = CourseCatalog.objects.get()
           coursecatalog.activateCourse(course)
           return HttpResponse(coursecatalog.activatedcourses.count())
