from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee
# Create your views here.
def greeting(response):
    s="<h1>CKMKB PKMKB this is landing page</h1>"
    return HttpResponse(s)
def employee_info_view(request):
    employees=Employee.objects.all()
    data={"employees":employees}
    return (render(request,"testapp/employees.html",data))
def about(request):
    text="This is an bout page"
    return render(request,"testapp/about.html",{"text":text})
def contact(response):
    s="<h1>CKMKB PKMKB this is contact page</h1>"
    return HttpResponse(s)
