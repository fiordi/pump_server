"""pump_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Adds a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#requests for OUR handlers
from course.views import ManageCourseHandler
from packet.views import ManagePacketHandler
from sale.views import ManageSaleHandler

urlpatterns.extend([
    url(r'^course/makenewcourse', ManageCourseHandler().makeNewCourse),
    url(r'^course/modifycourse', ManageCourseHandler().modifyCourse),
    url(r'^lesson/addlesson', ManageCourseHandler().addLesson),
])


#requests to be redirected to REST FRAMEWORK handlers
from django.conf.urls import url, include
from rest_framework import routers
from course.REST_classes import CourseViewSet, SingleLessonViewSet, RepeatedLessonViewSet
from packet.REST_classes import PacketViewSet
from sale.REST_classes import SaleViewSet
from subscription.REST_classes import CustomerViewSet, SubscriptionViewSet

router = routers.DefaultRouter()
router.register(r'course', CourseViewSet.CourseViewSet)
router.register(r'single-lesson', SingleLessonViewSet.SingleLessonViewSet)
router.register(r'repeated-lesson', RepeatedLessonViewSet.RepeatedLessonViewSet)
router.register(r'packet', PacketViewSet.PacketViewSet)
router.register(r'sale', SaleViewSet.SaleViewSet)
router.register(r'customer', CustomerViewSet.CustomerViewSet)
router.register(r'subscription', SubscriptionViewSet.SubscriptionViewSet)

urlpatterns.extend([
    url(r'^rest/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
])
