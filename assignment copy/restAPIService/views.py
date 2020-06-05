from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


from restAPIService.models import User

import requests
import math

def todoView(request):
    return HttpResponse("hello world")


def showTable(request):
    print(request,11111)
    response = requests.get('http://localhost:8000/api/user/')
    userData = response.json()

    if userData['meta']['total_count'] <= userData['meta']['limit']:
        pagesNeeded = 1
    else:
        pagesNeeded = userData['meta']['total_count'] // userData['meta']['limit']
    paginator = []
    for i in range(0, pagesNeeded):
        url = 'http://localhost:8000/showusers/user/{}' .format(i+1)
        paginator.append({"link" : url})
    firstAndLast = {"first" : 'http://localhost:8000/showusers/user/{}' .format(1), "last" : url}
    
    context = {'users' : userData['objects'], "paginator" : paginator, "firstAndLast" : firstAndLast}
    return render(request, "showTable.html", context)


def paginationView(request, page, pageNumber):

    tableUrl = "showusers"
    response = requests.get('http://localhost:8000/api/{}/' .format(page))
    metaData = response.json()

    offset = "?limit={}&offset={}".format(metaData['meta']['limit'], (int(pageNumber)-1)* metaData['meta']['limit'])
    link = 'http://localhost:8000/api/{}/{}' .format(page, offset)

    if metaData['meta']['total_count'] <= metaData['meta']['limit']:
        pagesNeeded = 1
    else:
        pagesNeeded = math.ceil(metaData['meta']['total_count'] / metaData['meta']['limit'])
    paginator = []
    for i in range(0, pagesNeeded):
        url = 'http://localhost:8000/{}/{}/{}' .format(tableUrl, page, i+1)
        paginator.append({"link" : url})
    firstAndLast = {"first" : 'http://localhost:8000/{}/{}/{}' .format(tableUrl, page, 1), "last" : url}
    response = requests.get(link)
    userData = response.json()
    context = {'users' : userData['objects'], "paginator" : paginator, "firstAndLast" : firstAndLast}
    return render(request, "showTable.html", context)



@csrf_exempt
def addInTable(request):
    if request.method == 'POST':
        if request.POST.get('firstName') and request.POST.get('lastName') and request.POST.get('email'):
            user=User()
            
            user.firstName= request.POST.get('firstName')
            user.lastName= request.POST.get('lastName')
            user.email = request.POST.get('email')
            print(user.firstName, user.lastName, user.email)
            if not User.objects.filter(email=user.email).exists():
                user.save()
                return HttpResponse("Entry Added")
            else:
                return HttpResponse("Already Present")


def removeInTable(request, id):
    isExist = User.objects.filter(id=id).exists()
    print(isExist)
    if isExist:
        user = User.objects.get(pk = id)
        is_deleted = User.id(null=False, default=False)
        print(is_deleted)
        user.delete()
        return redirect("http://localhost:8000/showusers/user")
    else:
        print("Data not present")
        return redirect("http://localhost:8000/showusers/user")
    
    