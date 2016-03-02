from django.http import HttpResponse
from django.views.generic import View

class ManageCourseHandler(View):

    def makeNewCourse(self, request):
       if request.method == 'GET':
           from Course import Course
           from CourseCatalog import CourseCatalog
           course = Course().createCourse(open = True)
           coursecatalog = CourseCatalog()
           coursecatalog.save()
           coursecatalog.addCourse(course)

           return HttpResponse('ciao')

    def setCourseInfo(self, request):
        if request.method == 'GET':
           from pump_app.model_classes import Course
           course = Course.createCourse()
           return course

    def addLesson(self, aWeekDay, aStartTime, aEndTime, aTrainer, aFrequency):
        pass

    def saveCourse(self):
        pass

    def activateCourse(self):
        pass
