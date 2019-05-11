"""SMS_PROJ1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from testapp.views import sms_register,sms_login,sms_package_create,sms_showallpackages,sms_updatepackage,sms_deletepackage,sms_home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^MyplexSMS/register',sms_register),
    url(r'^MyplexSMS/login',sms_login),
    url(r'^MyplexSMS/Home/',sms_home),
    url(r'^MyplexSMS/CreatePackage/',sms_package_create),
    url(r'^MyplexSMS/ShowAllPackages/',sms_showallpackages),
    # url(r'^MyplexSMS/ShowAllPackages/(?P<packageId>\d+)/',sms_showallpackages),
    url(r'^MyplexSMS/UpdatePackage/',sms_updatepackage),
    url(r'^MyplexSMS/DeletePackage/',sms_deletepackage),
    url(r'^',include('testapp.sms_api1.urls')),


]
