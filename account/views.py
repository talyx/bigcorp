from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django_email_verification import send_email
from .forms import UserCreateForm, LoginForm, UserUpdateForm


User = get_user_model()

#Register new user
def register_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_email = form.cleaned_data.get('email')
            user_name = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            
            #Create new user
            user = User.objects.create_user(
                username=user_name,
                email=user_email,
                password=user_password
            )
            user.is_active = False
            send_email(user)
            return redirect(reverse('account:email-verification-sent'))
    else:
        form = UserCreateForm()
    return render(request, 'account/registration/register.html', {'form': form})


def login_user(request):
    form = LoginForm()
    if request.user.is_authenticated:
        return redirect(reverse('shop:products'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('account:dashboard'))
        else:
            messages.error(request, 'Invalid username or password')
            return redirect(reverse('account:login'))
        
    context = {
        'form': form
    }
    return render(request, 'account/login/login.html', context)


def logout_user(request):
    logout(request)
    return redirect(reverse('shop:products'))


@login_required(login_url='account:login')
def dashboard_user(request):\
    return render(request, 'account/dashboard/dashboard.html')

@login_required(login_url='account:login')
def profile_user(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('account:dashboard'))
    else:
        form = UserUpdateForm(instance=request.user)
    
    context = {
        "form": form
    }
    return render(request, 'account/dashboard/profile-management.html', context)

@login_required(login_url='account:login')
def delete_user(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        user.delete()
        return redirect(reverse('shop:products'))
    
    return render(request, 'account/dashboard/account-delete.html')