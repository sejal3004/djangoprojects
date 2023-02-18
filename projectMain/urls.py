"""projectMain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from homeapp import views as v1    #for routing
from  fitnessapp import views as v2


urlpatterns = [
    path('admin/', admin.site.urls),
    path("hello/",v1.hello),
    path("bye/",v1.bye),
    path("hola/",v1.hola),
    path("legday/",v2.legday),
    path("cardio/",v2.cardio)

]
