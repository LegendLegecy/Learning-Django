"""
URL configuration for start project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('course/', views.course),
    path('course/<coursename>', views.coursedetails),
    path('dashboard/', views.index,name='home'),
    path('calculator/', views.calculator, name='calculator'),
    path('table/', views.table, name='table'),
    path('happy-birthday/', views.happybirthday, name='happy-birthday'),
    path('happy-birthday2/', views.happybirthday2, name='happy-birthday2'),
    path('product-list/', views.productlist, name='product-list'),
    path('product-detail/<title_slug>', views.productdetails ,name='product-details'),
    path('about-us', views.aboutus,name='about'),
    path('contact-us', views.contactus,name='contact'),
    path('sample-login', views.samplelogin,name='sample-login'),
    path('',views.signup,name='signup'),
    path('search/',views.search,name='search'),
]

# Only in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)