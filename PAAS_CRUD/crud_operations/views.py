from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from django.contrib import messages

# Create your views here.
def Create(request):
    print("Create called")
    if request.method == "POST":
        Name = request.POST['Name']
        USN = request.POST['USN']
        Branch = request.POST['Branch']

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
    if request.method == "POST":
        USN = request.POST['USN']
        New_Branch = request.POST['Branch']
        if not Student.objects.filter(pk=USN).exists():
            messages.info(request, "No student with USN {} exists in the database".format(USN))
        else:
            try:
                student = Student.objects.get(pk=USN)
                student.Branch = New_Branch
                student.save()
                messages.info(request, "Updated successfully")
            except:
                messages.info(request, "Could not find the student specified")            

        return render(request, 'crud_operations/crud_update.html')
    else:
        return render(request, 'crud_operations/crud_update.html') 

def Retrieve(request):
    if request.method == "POST":
        print(request.POST.keys())
        USN = request.POST['USN']

        if Student.objects.filter(pk=USN).exists():
            messages.info(request, "There exists a student with the USN {}".format(USN))
        else:
            messages.info(request, "No student with USN {} exists in the database".format(USN))

        return render(request, 'crud_operations/crud_retrieve.html')
    else:
        return render(request, 'crud_operations/crud_retrieve.html') 

def Delete(request):
    if request.method == "POST":
        print(request.POST.keys())
        USN = request.POST['USN']

        if Student.objects.filter(pk=USN).exists():
            temp = Student.objects.get(pk=USN)
            temp.delete()
            messages.info(request, "Deleted successfully")
        else:
            messages.info(request, "No student with USN {} exists in the database".format(USN))

        return render(request, 'crud_operations/crud_delete.html')
    else:
        return render(request, 'crud_operations/crud_delete.html') 
    
def index(request):
    return HttpResponse("Crud home page")