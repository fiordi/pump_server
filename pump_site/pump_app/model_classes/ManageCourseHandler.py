from django.http import HttpResponse
from django.views.generic import View
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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
        if request.method == 'POST':
            from pump_app.model_classes.Course import Course
            from pump_app.REST_classes.CourseSerializer import CourseSerializer
            serializer = CourseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
