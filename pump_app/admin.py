from django.contrib import admin

from pump_app.models import Course
from pump_app.models import CourseCatalog
from pump_app.models import SingleLesson
from pump_app.models import RepeatedLesson
from pump_app.models import Trainer

admin.site.register(Course)
admin.site.register(CourseCatalog)
admin.site.register(SingleLesson)
admin.site.register(RepeatedLesson)
admin.site.register(Trainer)
