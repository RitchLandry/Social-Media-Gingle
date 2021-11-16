from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

def Index(request,*arg,**kwargs):

    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate( username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index.html')
    context = {}
    return render(request,'local/base.html',context)

def registerUser(request,*arg,**kwargs):
    form = CreateUserForm()
    if request.method == "POST": 
        form = CreateUserForm(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('/')
    context = {
        'form':form
    }
    return render(request,'local/register.html',context)
