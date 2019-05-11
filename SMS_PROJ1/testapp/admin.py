from django.contrib import admin
from testapp.models import SMSRegister,SMSPackageDetails
class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','email','password1','password2']
admin.site.register(SMSRegister,RegisterAdmin)
class SMSPackageAdmin(admin.ModelAdmin):
    list_display=['packageId','packageName','commertial_model','contentType','coupansApplicable','startDate','endDate','duration','packDuration','packType','subscriptionType','packPremium','consumptionType','downloadType','description','packDataValue','assetGroupId','network_type','packageIndicator','ParentPackId','packValidatyPeriod','offerDescription','actionTobeTaken','activationReqLaunch','partnerId','imgUrl','offerImgUrl','unsubscription','actionButtonText','iosProductId','autoSubscribe','os','packStatus','targetAudience','offerId','cgSmsWifiEnabled','unsubdescription']
admin.site.register(SMSPackageDetails,SMSPackageAdmin)

# Register your models here.
