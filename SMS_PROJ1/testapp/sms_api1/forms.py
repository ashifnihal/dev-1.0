from django import forms
from testapp.models import SMSPackageDetails
class SMS_Package_ModelForm(forms.ModelForm):
    class Meta:
        model=SMSPackageDetails
        fields='__all__'
