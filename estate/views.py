from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request,'landing.html')
    
def properties(request):
    return render(request,'properties.html')
    
def agents(request):
    return render(request,'agents.html')
    
def about(request):
    return render(request,'about.html')
    
def contact(request):
    return render(request,'contact.html')
    