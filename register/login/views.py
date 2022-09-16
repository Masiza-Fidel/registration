from django.shortcuts import render,redirect
from  django.http import HttpResponse
from django.contrib.auth.models import user,auth
from django.contrib import messages
# Create your views here.
def register (request):
    if request.method=='POST':

      username=request.POST['username']
      email=request.POST['email']
      password=request.POST['password']
      password2=request.POST['password2']

      if password==password2:
           if user.objects.filter(email=email).exists():
               messages.info(request,"Email has already been used!")
               return redirect("register")
           elif user.objects.filter(username=username).exists():
               messages.info(request,"Username has already been used!")
               return redirect ("register")
           else:
                user=user.objects.create_user(username=username,email=email,password=password)  
                user.save(); 
                return redirect('login') 
      else:
          messages.info(request,'password not the Same')
          return redirect('register')
    else:      
        return render(request,"register.html")

def login (request):
    if request.method=='POST': 
       username=request.POST['username']
       password=request.POST['password']
       user= auth.authenticate (username=username,password=password)
    if user is not None:
         auth.login (request,user)
         return redirect('/')
    else:
            messages.info(request,'invalid credentials/') 
            return redirect('login')

    return render(request,'login.html')



