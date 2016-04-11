from django.contrib import admin

from pump_app.models import Course
from pump_app.models import CourseCatalog
from pump_app.models import SingleLesson
from pump_app.models import RepeatedLesson
from pump_app.models import Trainer
from pump_app.models import Activated
from pump_app.models import Deactivated
from pump_app.models import Trashed
from pump_app.models import Incomplete

admin.site.register(Course)
admin.site.register(CourseCatalog)
admin.site.register(SingleLesson)
admin.site.register(RepeatedLesson)
admin.site.register(Trainer)
admin.site.register(Trashed)
admin.site.register(Deactivated)
admin.site.register(Activated)
admin.site.register(Incomplete)

