from django.contrib import admin

from pump_app.models import Course
from pump_app.models import CourseCatalog
from pump_app.models import Lesson
from pump_app.models import Trainer

admin.site.register(Course)
admin.site.register(CourseCatalog)
admin.site.register(Lesson)
admin.site.register(Trainer)
