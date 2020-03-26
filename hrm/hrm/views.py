# Rahul

from django.shortcuts import render


class Employee:
    id: int
    fname: str
    lname: str


def index(request):
    # return HttpResponse('Hello')
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html', {'name': 'This is Employee Management System'})


def employee(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    Employee.fname = fname
    Employee.lname = lname
    Employee.id = 1010

    return render(request, 'index.html', {'employee': Employee})
