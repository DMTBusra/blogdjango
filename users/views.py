from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.urls import reverse_lazy
from .form import UserForm,ProfileForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
from  .models import User
# from django.views.generic import UpdateView

def home(request):
    return render(request, 'users/home.html')
def register(request):
    form = UserForm()

    if request.method == 'POST':
        # pass in post data when instantiate the form.
        form = UserForm(request.POST, request.FILES)
        # if the form is ok with the info filled:
        if form.is_valid():
            form.save()
            # that creates a new user
            # after creation of the user, want to authenticate it
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # inspect the page and see the first password is password1, import authenticate
            user = authenticate(username=username, password=password)

            # want user to login right after registered, import login
            login(request, user)
            # want to redirect to home page, import redirect
            return redirect('home')

    context = {
        'form_user': form
    }

    return render(request, "users/register.html", context)
def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('home')
def user_login(request):

    form = AuthenticationForm(request, data=request.POST)

    if form.is_valid():
        user = form.get_user()
        if user:
            messages.success(request, "Login successfull")
            login(request, user)
            return redirect('home')
    return render(request, 'users/user_login.html', {"form": form})
def newpost(request):
    return render(request, 'users/newpost.html')
# def profile(request):

#     return render(request, 'users/profile.html')

def profile_update(request, id):

    user = User.objects.get(id=id)

    form = ProfileForm(instance=user)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated!!l")
            return redirect("home")

    context= {

        
        "form":form
    }

    return render(request, "users/profile.html", context)


# class UserProfileView(UpdateView):
#     model=User
#     form_class =UserForm
#     template_name="users/profile.html"
#     success_url=reverse_lazy("home")