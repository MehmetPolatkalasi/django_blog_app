from tkinter.tix import Form
from django.shortcuts import render,redirect

from .forms import LoginForm, RegisterForm

from django.contrib.auth.models import User

from django.contrib.auth import login,authenticate,logout

from django.contrib import messages

# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
            
        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)

        messages.info(request,"Başarıyla Kayıt Oldunuz")

        return redirect("index")
        
    context = {
            "form":form
        }
    return render(request,"register.html",context)





    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)

            return redirect("index")
        
        context = {
            "form":form
        }
        return render(request,"register.html",context)


    else:
        form = RegisterForm()
        context = {
            "form":form
        }
        return render(request,"register.html",context)"""

    """
    form = RegisterForm()
    context = {
        "form": form
    }
    return render(request,"register.html",context)"""

def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form": form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)

        messages.success(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
            

    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Başarıyla Çıkış Yaptınız")
    return redirect("index")
