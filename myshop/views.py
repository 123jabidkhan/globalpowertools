from django.shortcuts import render
from .forms import RegisterForm, QueryForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.models import User
from .models import Query

# Create your views here.
# home
def home(request):
    return render(request,'myshop/home.html')
# aobout
def about(request):
    return render(request,'myshop/about.html')

# contact
def contact(request):
    return render(request,'myshop/contact.html')
# RegisterForm
def register(request):
    if request.method == 'POST':
        form  = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'Your acoount created succesfully!!')
            return HttpResponseRedirect('/register/')
            
    else:
        form = RegisterForm()
    return render(request,'myshop/register.html',{'form':form})
                    

# user_login view
def user_login(request):
    if not request.user.is_authenticated:
    
        if request.method == 'POST':
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user  = authenticate(request,username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.success(request,'You logged succesfully!!')
                    return HttpResponseRedirect('/profile')                                             
        else:
            form = AuthenticationForm()
            return render(request, 'myshop/login.html',{'form':form})
    else:
        return HttpResponseRedirect('/profile/')
        

# profile
def profile(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            n=form.cleaned_data['name']
            p=form.cleaned_data['phone']
            a=form.cleaned_data['address']
            query=Query(name=n,phone=p,address=a)
            query.save()
            form=QueryForm()            
            messages.success(request,'Your query recived successfully...!!')
            return HttpResponseRedirect('/profile/')
    else:
        form=QueryForm()
    return render(request,'myshop/profile.html',{'form':form}) 
        
# admin_login
def admin_login(request):
    if request.method == 'POST':
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(username=u,password=p)
        if user is not None:
            if user.is_staff:
                login(request,user)
                messages.success(request,'Admin Logged Successfully..!!')
                return HttpResponseRedirect('/admin_profile/')
        else:
            messages.warning(request,'username and password not match..Pleace try again')
            return HttpResponseRedirect('/admin_login/')
    else:
        return render(request,'myshop/admin.html')
# admin_profile
def admin_profile(request):
    querys=Query.objects.all()
    return render(request,'myshop/admin_profile.html',{'querys':querys})

# user_delete
def user_delete(request,id):
    pi=Query.objects.get(id=id)
    pi.delete()
    return HttpResponseRedirect('/admin_profile/')    
# logout view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')