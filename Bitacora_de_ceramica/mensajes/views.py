from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mensaje
from django.contrib.auth.models import User
from .forms import MensajeForm
from django.contrib import messages


@login_required
def inbox_view(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-timestamp')
    return render(request, 'mensajes/inbox.html', {'mensajes': mensajes})


@login_required
def enviar_mensaje_view(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, "Mensaje enviado con éxito.")
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/enviar_mensaje.html', {'form': form})


@login_required
def enviar_mensaje_a_view(request, username):
    destinatario = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.destinatario = destinatario
            mensaje.save()
            return redirect('inbox')
    else:
        form = MensajeForm()
    return render(request, 'mensajes/enviar_mensaje.html', {
        'form': form,
        'destinatario': destinatario,
    })

@login_required
def borrar_mensaje_view(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk, destinatario=request.user)
    if request.method == 'POST':
        mensaje.delete()
        messages.success(request, "Mensaje eliminado con éxito.")
        return redirect('inbox')
    return render(request, 'mensajes/confirmar_borrado.html', {'mensaje': mensaje})
