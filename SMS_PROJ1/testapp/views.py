from django.shortcuts import render
from django.http import HttpResponse
from testapp.forms import RegisterForm,LoginForm,PackageDetailsForm
from testapp.models import SMSRegister,SMSPackageDetails


def sms_register(request):
    form=RegisterForm()
    if request.method=='POST':
        form=RegisterForm(request.POST)
        print('@@form',form)
        try:

            if form.is_valid():
                first_name=form.cleaned_data['first_name']
                last_name=form.cleaned_data['last_name']
                email=form.cleaned_data['email']
                password1=form.cleaned_data['password1']
                password2=form.cleaned_data['password2']
                if password1==password2:
                    print('@@password1',password1,'@@password2',password2)
                    datareg=SMSRegister.objects.get_or_create(first_name=first_name,last_name=last_name,email=email,password1=password1,password2=password2)
                    print('@@datareg',datareg)
                    lform=LoginForm()
                    return render(request,'testapp/login.html',context={'form':lform})
                else:
                    return HttpResponse('both password1 & password2 must be match')
        except:
            print('@@form.errors',form.errors)

    return render(request,'testapp/home.html',context={'form':form})
    # return HttpResponse('bhfgjglgdl')
def sms_login(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            try:
                rdata=SMSRegister.objects.get(email=email)
                print('@@rdata',rdata)
                oemail=rdata.email
                opassword=rdata.password1
                print('@@oemail',oemail,'@@opassword',opassword)
                if str(password)==str(opassword) and str(email)==str(oemail):
                    print('login success')
                    return render(request,'testapp/welcomepage.html')
                else:
                    print('login failed plese reneter valid email id and password...')
            except SMSRegister.DoesNotExist:
                return HttpResponse('no records found for this email id...')

    return render(request,'testapp/login.html',context={'form':form})

def sms_home(request):
    return render(request,'testapp/welcomepage.html')

def sms_package_create(request):
    form=PackageDetailsForm()
    if request.method=='POST':
        form=PackageDetailsForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'testapp/welcomepage.html')

    return render(request,'testapp/createpackage.html',context={'form':form})
def sms_showallpackages(request):
    qs=SMSPackageDetails.objects.all()
    id=request.GET.get('packageId',None)
    if id!=None:
        print('@@id',id)
        qs=SMSPackageDetails.objects.get(packageId=id)
        print('@@qs',qs)
        return render(request,'testapp/showpackagesbypackid.html',context={'packagedetails':qs})

    return render(request,'testapp/showpackages.html',context={'packagedetails':qs})

def sms_updatepackage(request):
    print('fdsfbgbgdsgbbv.b')
    id=request.GET.get('packageId',None)
    print('@@@id',id)
    if id!=None:
        print('@@id',id)
        try:
            qs=SMSPackageDetails.objects.get(packageId=id)
            print('@@@qs',qs)
            if request.method=='POST':
                form=PackageDetailsForm(request.POST,instance=qs)
                # print('@@form',form)
                if form.is_valid():
                    print('@@@form.is_valid')
                    form.save()
                    return HttpResponse('record updated Successfully...ss')
                if form.errors:
                    print('@@@form.errors',form.errors)
                    return HttpResponse('from errors')
            return render(request,'testapp/updatepackagedetailsbyid.html',context={'form':qs})
        except SMSPackageDetails.DoesNotExist:
            return HttpResponse('No records found for this ID...')

    else:
        return HttpResponse('please provide id to get the data...')
def sms_deletepackage(request):
    id=request.GET.get('packageId',None)
    if id!=None:
        try:
            qs=SMSPackageDetails.objects.get(packageId=id)
            data=qs.delete()
            print('@@deletedata',data)
            return HttpResponse('record deleted Successfully..')
        except SMSPackageDetails.DoesNotExist:
            return HttpResponse('No records found for this ID...')








# Create your views here.
