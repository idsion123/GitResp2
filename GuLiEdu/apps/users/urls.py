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
from . import  views
urlpatterns = [
    re_path(r'^user_register/$',views.user_register,name='user_register'),
    re_path(r'^user_login/$',views.user_login,name='user_login'),
    re_path(r"^user_logout/$",views.user_logout,name='user_logout'),
    re_path(r'^user_active/(\w+)/$',views.user_active,name='user_active'),
    re_path(r'^user_forget/$',views.user_forget,name='user_forget'),
    re_path(r'^user_reset/(\w+)/$',views.user_reset,name='user_reset'),
    re_path(r'^user_info/$',views.user_info,name='user_info'),
    re_path(r'^user_changeimage/$',views.user_changeimage,name='user_changeimage'),
    re_path(r'^user_changeinfo/$',views.user_changeinfo,name='user_changeinfo'),
    re_path(r'^user_changeemail/$',views.user_changeemail,name='user_changeemail'),
    re_path(r'^user_resetemail/$',views.user_resetemail,name='user_resetemail'),
    re_path(r'^user_mycourse/$',views.user_mycourse,name='user_mycourse'),
    re_path(r'^user_fav_org/$',views.user_fav_org,name='user_fav_org'),
    re_path(r'^user_fav_teacher/$',views.user_fav_teacher,name='user_fav_teacher'),
    re_path(r'^user_fav_course/$',views.user_fav_course,name='user_fav_course'),
    re_path(r'^user_mymsg/$',views.user_mymsg,name='user_mymsg'),





]
