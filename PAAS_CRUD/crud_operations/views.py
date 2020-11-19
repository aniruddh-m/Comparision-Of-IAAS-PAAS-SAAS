from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.contrib import messages

# Create your views here.
def Create(request):
    print("Create called")
    if request.method == "POST":
        print(request.POST.keys())
        Name = request.POST['Name']
        USN = request.POST['USN']
        Branch = request.POST['Branch']
        print(Name, USN, Branch)

        if Student.objects.filter(pk=USN).exists():
            messages.info(request, "There already exists a student with the USN {}".format(USN))
        else:
            s1 = Student(Name=Name, USN=USN, Branch=Branch)
            s1.save()
            messages.info(request, "The student {} was added successfully".format(Name))

        return render(request, 'crud_operations/crud_create.html')
    else:
        return render(request, 'crud_operations/crud_create.html')

def Update(request):
    return 

def Retrieve(request):
    return 

def Delete(request):
    return 
    
def index(request):
    return HttpResponse("Crud home page")