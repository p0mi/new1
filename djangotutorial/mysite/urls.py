"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from polls.nocodb_utils_v2 import get_nocodb_data
from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
       openapi.Info(
           title="My API",
           default_version='v1',
           description="API documentation for My Django Project",
       ),
       public=True,
       permission_classes=(permissions.AllowAny,),
   )

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


