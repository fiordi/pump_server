from django.contrib import admin

from course.models import Course
from course.models import CourseCatalog
from course.models import SingleLesson
from course.models import RepeatedLesson


admin.site.register(Course)
admin.site.register(CourseCatalog)
admin.site.register(SingleLesson)
admin.site.register(RepeatedLesson)

