from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm, UserForm
from .models import Perfil

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Perfil.objects.get_or_create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def perfil_view(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html', {'perfil': perfil})

@login_required
def editar_perfil(request):
    user_form = UserForm(instance=request.user)
    perfil_form = PerfilForm(instance=request.user.perfil)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('perfil')

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'perfil_form': perfil_form
    })

@login_required
def cambiar_contraseña(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('perfil')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'accounts/change_password.html', {'form': form})

from pages.models import Pieza

@login_required
def crear_pieza(request):
    if request.method == 'POST':
        form = PiezaForm(request.POST, request.FILES)
        if form.is_valid():
            pieza = form.save(commit=False)
            pieza.autor = request.user
            pieza.save()
            return redirect('lista_piezas')
    else:
        form = PiezaForm()
    return render(request, 'accounts/crear_pieza.html', {'form': form})

def lista_piezas(request):
    piezas = Pieza.objects.all().order_by('-fecha')
    return render(request, 'accounts/lista_piezas.html', {'piezas': piezas})
