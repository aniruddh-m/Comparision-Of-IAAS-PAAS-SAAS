from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Create(request):
    return render(request, 'crud_operations/crud_template.html')
    
def Update(request):
    return 

def Retrieve(request):
    return 

def Delete(request):
    return 
    
def index(request):
    return HttpResponse("Crud home page")