from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from .forms import UserRegisterForm
from django.contrib.auth.models import User
def home_page(request):
    return render(request,'portfolio.html')
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


class UserRegisterView(TemplateView):
    form_class=UserRegisterForm
    model=User
    template_name ="registration.html"
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return redirect("error")