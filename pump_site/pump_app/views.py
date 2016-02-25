from django.shortcuts import render
from django.views.generic import View
from pump_app.models import Course
import datetime

class Debug(View):
    def get(self, request):
        startDate = datetime.date(2016, 2, 1)
        endDate = datetime.date(2018, 2, 1)
        startTime = datetime.time(10, 1)
        endTime = datetime.time(11, 1)
        frequency = 14
        course = Course()
        course.addLesson(startDate, endDate, startTime, endTime, frequency)

# Create your views here.
