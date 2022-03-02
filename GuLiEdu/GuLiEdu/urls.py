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
# """
import xadmin
from django.views.static import serve
from xadmin.plugins import xversion
xadmin.autodiscover()
from django.contrib import admin
from django.urls import path,re_path,include
xversion.register_models()
from users import views
from  .settings import MEDIA_ROOT
urlpatterns = [
    re_path(r'^xadmin/', xadmin.site.urls),
    re_path(r'^captcha/',include('captcha.urls')),
    re_path(r'^users/',include(('users.urls','users'),namespace='users')),
    re_path(r'^courses/',include(('courses.urls','courses'),namespace='courses')),
    re_path(r'^orgs/',include(('orgs.urls','orgs'),namespace='orgs')),
    re_path(r'^operations/',include(('operations.urls','operations'),namespace='operations')),
    re_path(r"^$",views.index,name='index'),
    # media
    re_path(r'^media/(?P<path>.*)$',serve,{"document_root": MEDIA_ROOT}),

]
handler404 = 'users.views.handler_404'
handler500 = 'users.views.handler_500'
