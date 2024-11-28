"""
URL configuration for Filmindustry project.

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
from django.urls import path,include
import bollywood,tollywood
from kollywood.views import *
from hollywood.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bollywood/',include('bollywood.urls')),
    path('tollywood/',include('tollywood.urls')),
    path('thalapathy/',thalapathy,name='thalapathy'),
    path('superstar/',superstar,name='superstar'),
    path('actionking/',actionking,name='actionking'),
     path('marvelking/',marvelking,name='marvelking'),


]
