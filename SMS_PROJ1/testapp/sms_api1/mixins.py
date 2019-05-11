from django.core import serializers
import json
class PackageMixin(object):
    def package_serializer(self,data):
        package_serializer=serializers.serialize('json',data)
        pdata=json.loads(package_serializer)
        print('@@pdata',pdata)
        list_data=[]
        for obj in pdata:
            obj_data=obj['fields']
            list_data.append(obj_data)
        return list_data
