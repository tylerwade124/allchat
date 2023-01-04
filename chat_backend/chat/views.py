from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
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