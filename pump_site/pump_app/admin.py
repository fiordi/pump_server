from django.contrib import admin

from pump_app.models import Course
from pump_app.models import CourseCatalog

admin.site.register(Course)
admin.site.register(CourseCatalog)