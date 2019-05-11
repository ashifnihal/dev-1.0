from testapp.models import SMSPackageDetails
from django.views import View
from testapp.sms_api1.mixins import PackageMixin
from django.shortcuts import render
from django.http import HttpResponse
import json
class SMSApiView1(View,PackageMixin):
    def get(self,request,*args,**kwargs):
        qdata=SMSPackageDetails.objects.all()
        pdata=self.package_serializer(qdata)
        jdata=json.dumps(pdata)
        return HttpResponse(jdata,content_type='application/json')
