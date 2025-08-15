"""
URL configuration for WS project.

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
from . import views
# OR WE CAN USE "from APP-NAME import views"

urlpatterns = [
    path("admin/", admin.site.urls , name="admin"),
    path("about-us/", views.aboutus , name="about"),
    path("contact/", views.contact , name="contact"),
    path("offers/", views.offers , name="offers"),
    # DYNAMIC URL
    # Also we can specify data-types like "< str: CourseName >"
    path("course/<CourseName>/", views.Course_Name), 

    path("", views.home),
    path("Happy-Birthday/", views.Happy_Birthday),
    path("Happy-Birthday2/", views.Happy_Birthday2),
    path("dashboard/", views.dashboard , name="dashboard"),
    path("login/", views.login , name="login"),
    path("calculator/", views.calculator , name="calculator"),
    path("even-odd/", views.even_odd , name="even-odd"),
    path("marksheet/", views.marksheet , name="marksheet"),
]
