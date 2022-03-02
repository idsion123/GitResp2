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
re_path(r'^user_ask/$',views.user_ask,name='user_ask'),
re_path(r"^user_love/$",views.user_love,name='user_love'),
re_path(r"^user_delete/$",views.user_delete,name='user_delete'),
re_path(r"^user_comment/$",views.user_comment,name='user_comment'),
re_path(r"^msg_delete/$",views.msg_delete,name='msg_delete'),

]
