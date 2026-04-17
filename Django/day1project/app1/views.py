from django.shortcuts import render
from django.http  import HttpResponse
import random

# Create your views here.


# Home 
###   create a function in views.py and will be linking to the URL (project folder) -   
### Function - logic or code

def home(request):
    user_dict = {
       'name': "Tarun",
       'age' : 10,
       'login_status' : False
    }
    
    return  render(request,'home.html',{'user_data':user_dict})

# About us 

def About_us(request):
    randomnumber = random.randint(10,100)
    
    return render(request,'about-us.html',{'rand_num':randomnumber})

# Work From Home
def work_from_home(request):
    return HttpResponse("<h1>This is a work from home page  , </h1><p>In this page you will get all the work from home jobs </p><p>You can apply for the jobs and get the job </p>")

# Contact
def contact(request):
    return HttpResponse("<h1>This is a contact page </h1>")

# Latest jobs
def latest_jobs(request):
    return HttpResponse("<h1>This is a latest jobs page </h1>")


# Any graduate jobs 
def any_graduate_jobs(request):
    return HttpResponse("<h1>This is a any graduate jobs page </h1>")

# Privacy policy
def privacy_policy(request):
    return HttpResponse("<h1>This is a privacy policy page </h1>")