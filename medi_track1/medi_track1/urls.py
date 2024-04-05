"""
URL configuration for medi_track1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings

from drf_spectacular.views import *
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('user.urls')),
   
    path('medi_track/schema/',SpectacularAPIView.as_view(),name='schema'),
    path('medi_track/schema/docs/',SpectacularSwaggerView.as_view(url_name='schema')),

]

if  settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, documents_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL, documents_root=settings.STATIC_ROOT)