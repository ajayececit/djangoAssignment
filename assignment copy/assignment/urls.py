"""assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restAPIService.views import todoView, addInTable, removeInTable, showTable, paginationView

from restAPIService.resources import (
    UserResource,
    UserResourceSortFirstName, 
    UserResourceSortLastName 
)
user_resource = UserResource()
user_resource_sort_first = UserResourceSortFirstName()
user_resource_sort_last = UserResourceSortLastName()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', todoView),
    path('showusers/user', showTable),
    path('showusers/<page>/<pageNumber>/', paginationView),
    path('addusers/', addInTable),
    path('removeuser/<id>', removeInTable),
    path('api/', include(user_resource.urls)),
    path('api/', include(user_resource_sort_first.urls)),
    path('api/', include(user_resource_sort_last.urls)),
    
    #path('test/', todoView),
]
