from django.conf.urls import url, include
from django.contrib import admin

from app import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'appointments', views.AppointmentViewSet)
router.register(r'patients', views.PatientViewSet)
router.register(r'procedure', views.ProcedureViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
