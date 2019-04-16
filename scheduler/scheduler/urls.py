from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers

from app.views import (
    AppointmentViewSet, PatientViewSet, ProcedureViewSet
)


router = routers.DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'procedures', ProcedureViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
