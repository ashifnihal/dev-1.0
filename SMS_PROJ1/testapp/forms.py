from testapp.models import SMSPackageDetails
from django import forms
class RegisterForm(forms.Form):
    first_name=forms.CharField(max_length=40)
    last_name=forms.CharField(max_length=40)
    email=forms.EmailField()
    password1=forms.CharField(max_length=30,widget=forms.PasswordInput)
    password2=forms.CharField(max_length=30,widget=forms.PasswordInput)
class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)
class PackageDetailsForm(forms.ModelForm):
    class Meta:
        model=SMSPackageDetails
        fields='__all__'
