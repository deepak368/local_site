from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def home_page(request):
    return render(request,'home.html')
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
            ...
        else:
            messages.success(request,("ther was error in login"))
            return redirect('home')
            
    else:
        return render(request,'authentication/login.html',{})
def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request,user)
            messages.success(request,("registration sucsess"))
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request,'authentication/register.html',{
        'form':form
    })
def logout_user(request):
    logout(request)
    messages.success(request,("you just logedout"))
    return redirect('home')
