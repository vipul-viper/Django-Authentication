from django.shortcuts import render,redirect
from .forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'app4/index.html')
def register(request):
    registered=False
    if request.method=='POST':
        uform=UserForm(data=request.POST)
        pform=UserProfileInfoForm(data=request.POST)
        if uform.is_valid() and pform.is_valid():
            user=uform.save()
            user.set_password(user.password)
            user.save()
            profile=pform.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()
            registered=True
        else:

            print(uform.errors,pform.errors)
    else:
        uform=UserForm()
        pform=UserProfileInfoForm()

    return render(request,'app4/registration.html',{'user_form':uform,'profile_form':pform,'registered':registered})
def userlogin(request):
   if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(username=username,password=password)
       if user:
           if user.is_active:
               login(request,user)
               return redirect('/')
           else:
               return HttpResponse("your account is inactive")
       else:
         return HttpResponse("invalid login details")
   else:
      return render(request,'app4/login.html',{})
@login_required
def userlogout(request):
    logout(request)
    return redirect('/')