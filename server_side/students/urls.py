  
from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'students', views.StudentsViewSet)
router.register(r'fees', views.FeesViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]