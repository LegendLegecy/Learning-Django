"""
URL configuration for mysite project.

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
from django.urls import path
from . import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",main.index , name= "index"),
    path("about",main.about , name= "about"),
    path("personal-navigator",main.PersonalNagivator , name= "personal-navigator"),
    path("home",main.home , name= "home"),
    path("analyze",main.analyze , name= "analyze"),
    path("result",main.result , name= "result"),
    path("template",main.template , name= "template"),
    path("text-analyzer",main.text_analyzer , name= "text-analyzer"),
    path("analyzed",main.analyzed , name= "analyzed"),
    path("about-us",main.about_us , name= "about-us"),
    path("contact-us",main.contact_us , name= "contact-us"),

]
