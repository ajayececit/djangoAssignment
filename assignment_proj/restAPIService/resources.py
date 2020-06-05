# restApiService/resources.py

from tastypie.resources import ModelResource
from .models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        #fields = ['firstName']
        limit = 2


class UserResourceSortFirstName(ModelResource):
    class Meta:
        queryset = User.objects.all().order_by("firstName")
        resource_name = 'sortfirstname'
        #fields = ['firstName']
        limit = 2


class UserResourceSortLastName(ModelResource):
    class Meta:
        queryset = User.objects.all().order_by("lastName")
        resource_name = 'sortlastname'
        #fields = ['firstName']
        limit = 2

