# # Create your views here.
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
import random
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect

from .forms import BlogForm
from .models import Blog
import datetime

def signin(request):
    return render(request,"signin.html") 

def signin_verification(request):
     if request.method=="POST":
        email=request.POST["email"]
        request.session["user_email"]=email
        if User.objects.filter(email=email).exists():
                send_otp(request)
                return render(request,'otp.html',{"email":email})
        else:
            nameuser=User(username=request.session['user_email'],email=request.session['user_email'])
            nameuser.save()
            send_otp(request)
            return render(request,'otp.html',{"email":email})                                        
     else:
        return HttpResponse("No Page")

def send_otp(request):
    s=""
    for x in range(0,6):
        s+=str(random.randint(0,9))
    request.session["otp"]=s
    send_mail("otp for sign up",s,'onlinetrainingnumber1@gmail.com',[request.session['user_email']],fail_silently=False)
    return render(request,"otp.html")

def  otp_verification(request):
    if  request.method=='POST':
        otp_=request.POST.get("otp")
    if otp_ == request.session["otp"]:
        #request.session["user_email"]=user_email
        return render(request,'secure.html')
    else:
        messages.error(request,"otp doesn't match")
        return render(request,'otp.html')

def logout_page(request):
    logout(request)
    return redirect('http://localhost:8000/')

def secure(request):    
    if request.user.is_authenticated:
        return HttpResponseRedirect('secure')
    return render(request,'http://localhost:8000/')
    
# Create Blog
def create_blog(request):
    user_email = request.session['user_email']    
    if request.method == "POST":
        Name = request.POST['Name']
        Advocate = request.POST['Advocate']
        Mobile = request.POST['Mobile']
        Email = request.POST['Email']
        CaseNo = request.POST['CaseNo']
        CaseYear = request.POST['CaseYear']
        CaseType = request.POST['CaseType']
        CourtName = request.POST['CourtName']
        CourtArea = request.POST['CourtArea']
        now = datetime.datetime.now()
        request.session["user_email"]=user_email
        data = Blog(Name=Name,Advocate=Advocate,Mobile=Mobile,Email=Email,CaseNo=CaseNo,CaseYear=CaseYear,CaseType=CaseType,CourtName=CourtName,CourtArea=CourtArea,Created_By=Name,Created_Date=now,user_email=user_email)
        data.save()
        return render(request,'secure.html')
    else:
        return render(request, 'insert.html')

# Retrive Employee
        
def show_blogs(request):
    user_email = request.session['user_email']    
    #blogs = Blog.objects.all()
    #blogs = Blog.objects.get(user_email=user_email)
    blogs = Blog.objects.filter(user_email=user_email).values()
    #request.session["blogs"]=blogs
    return render(request,'show.html',{'blogs':blogs} )
    #return render(request,"show.html")
    #return HttpResponse(blogs, content_type="application/json")
    #return render(request, 'secure.html', {'blogs': blogs})
    #return JsonResponse({'blogs': list(blogs)}, safe=False)