"""GuLiEdu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,re_path,include
from . import views

urlpatterns = [
    re_path(r'^org_list/$',views.org_list,name='org_list'),
    re_path(r'^org_detail/(\d+)/$',views.org_detail,name='org_detail'),
    re_path(r"^org_detail_course/(\d+)/$",views.org_detail_course,name='org_detail_course'),
    re_path(r"^org_detail_desc/(\d+)/$",views.org_detail_desc,name='org_detail_desc'),
    re_path(r"^org_detail_teachers/(\d+)/$",views.org_detail_teachers,name='org_detail_teachers'),
    re_path(r'^teacher_list/$',views.teacher_list,name='teacher_list'),
    re_path(r'^teacher_detail/(\d+)/$',views.teacher_detail,name='teacher_detail'),
]
