from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

# Create your views here.
def loginUser(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None: 
            login(request, user)
            return redirect('lobby')

    return render(request, 'chat/login_register.html', {'page': page})

def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()


            user = authenticate(request, username=user.username, password=request.POST['password1'])
            if user is not None:
                login(request, user)
                return redirect('lobby')

    context= {'form': form, 'page': page}
    return render(request, 'chat/login_register.html', context)

def home(request):
    return render(request, 'chat/home.html')


@login_required(login_url='login')
def lobby(request):
    return render(request, 'chat/lobby.html')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'chat/change_password.html', {
        'form': form
    })
User = get_user_model()

class UserDelete(DeleteView):
    model = User
    success_url = reverse_lazy('home')
    template_name = 'user_confirm_delete.html'

