from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserAuthForm

#   Views for Accounts application

def sign_up_view(request):

    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        form = UserAuthForm()
        if request.method == "POST":
            form = UserAuthForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Message to: " + user)
                return redirect('login')

        context = {"form": form}
        return render(request, "accounts/sign_up.html", context)

def user_logging_in(request):

    if request.user.is_authenticated:
        return redirect('home_page')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home_page')

        context = {}
        return render(request, "accounts/login.html", context)

def user_logging_out(request):
    logout(request)
    return redirect("login")