from django.contrib import admin

from pump_app.models import Course
from pump_app.models import CourseCatalog
from pump_app.models import Lesson

admin.site.register(Course)
admin.site.register(CourseCatalog)
admin.site.register(Lesson)