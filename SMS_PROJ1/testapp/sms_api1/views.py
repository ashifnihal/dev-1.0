from testapp.models import SMSPackageDetails
from django.views import View
from testapp.sms_api1.mixins import PackageMixin
from testapp.sms_api1.forms import SMS_Package_ModelForm
from django.shortcuts import render
from django.http import HttpResponse
import json
class SMSApiView1(View,PackageMixin):
    def get(self,request,*args,**kwargs):
        qdata=SMSPackageDetails.objects.all()
        pdata=self.package_serialize(qdata)
        jdata=json.dumps(pdata)
        return HttpResponse(jdata,content_type='application/json')
    def post(self,request,*args,**kwargs):
        rdata=request.body
        pdata=json.loads(rdata)
        form=SMS_Package_ModelForm(pdata)
        print('@@formdata',form)
        if form.is_valid():
            form.save(commit=True)
            jdata=json.dumps({'msg':'record inserted successfully'})
            return HttpResponse(jdata,content_type='application/json')
        if form.errors:
            jdata=json.dumps(form.errors)
            return HttpResponse(jdata,content_type='application/json')
