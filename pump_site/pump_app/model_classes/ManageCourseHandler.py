from django.http import HttpResponse
from django.views.generic import View

class ManageCourseHandler(View):

    def makeNewCourse(self, request):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           course = Course().createCourse(open = False)
           coursecatalog = CourseCatalog() # to be continued
           coursecatalog.addCourse(course)
           return HttpResponse('ciao')

    def setCourseInfo(self, request):
        if request.method == 'GET':
           from pump_app.model_classes import Course
           return course

    def addLesson(self, aWeekDay, aStartTime, aEndTime, aTrainer, aFrequency):
        pass

    def saveCourse(self):
        pass

    def activateCourse(self, request, id_course):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           course = Course.objects.get(pk = id_course)
           coursecatalog = CourseCatalog.objects.get()
           coursecatalog.activateCourse(course)
           return HttpResponse(id_course)
