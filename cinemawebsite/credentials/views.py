from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        repassword = request.POST['repassword']
        email = request.POST['email']
        if password == repassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,
                                                password=password)
                user.save()
                print("user created")
        else:
            messages.info(request, "password incorrect")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, "Register.html")


def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid username")
            return redirect('login')

    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
