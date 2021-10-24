"""server_side URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include

# import rest_framework views for get_token & refresh_token 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/blog/', include('blog.urls')),
    path('api/discussionforum/', include('discussionforum.urls')),
    path('api/academic/', include('students.urls')),
    # add simple-jwt urls
    path('api/gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
]
