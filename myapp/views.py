from django.shortcuts import render
from django.http import request
from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact,Feedback
from django.contrib import messages

# Create your views here.
def abc(request):
    
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
   


def contact(request):
    
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        messages.success(request,'submitted suucessfully')
        contact.save()
    return render(request,'contact.html')
 

def services(request):
    return render(request,'services.html') 

def feedback(request):
    if request.method=="POST":
        
        feedback=request.POST.get('feedback')
        feedback=Feedback(feedback=feedback)
        messages.success(request,'submitted suucessfully')
        feedback.save()
        
         
    return render(request,'feedback.html') 
# Create your views here.
