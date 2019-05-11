from django.conf.urls import url
from django.contrib import admin
from testapp.sms_api1.views import SMSApiView1
urlpatterns = [
url(r'^api1/',SMSApiView1.as_view())
]
