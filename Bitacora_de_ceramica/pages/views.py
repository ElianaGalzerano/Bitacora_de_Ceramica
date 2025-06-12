from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Pieza



class ListaPiezas(ListView):
    model = Pieza
    template_name = 'pages/lista_piezas.html'
    context_object_name = 'piezas'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(titulo__icontains=query)
        return queryset



class DetallePieza(DetailView):
    model = Pieza
    template_name = 'pages/detalle_pieza.html'
    context_object_name = 'pieza'


class CrearPieza(LoginRequiredMixin, CreateView):
    model = Pieza
    template_name = 'pages/pieza_form.html'  # ← ESTE NOMBRE es el que existe
    fields = ['titulo', 'tecnica', 'descripcion', 'imagen']
    success_url = reverse_lazy('lista_piezas')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)



class EditarPieza(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pieza
    template_name = 'pages/formulario_pieza.html'
    fields = ['titulo', 'tecnica', 'descripcion', 'imagen']
    success_url = reverse_lazy('lista_piezas')

    def test_func(self):
        pieza = self.get_object()
        return self.request.user == pieza.autor


class BorrarPieza(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pieza
    template_name = 'pages/borrar_pieza.html'
    success_url = reverse_lazy('lista_piezas')

    def test_func(self):
        pieza = self.get_object()
        return self.request.user == pieza.autor
    
    from django.contrib import messages
from django.shortcuts import redirect

class BorrarPieza(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pieza
    template_name = 'pages/borrar_pieza.html'
    success_url = reverse_lazy('lista_piezas')

    def test_func(self):
        pieza = self.get_object()
        return self.request.user == pieza.autor

    def handle_no_permission(self):
        messages.error(self.request, "No tenés permiso para borrar esta pieza porque no sos su autor.")
        return redirect('lista_piezas')



class AcercaDeMiView(TemplateView):
    template_name = 'pages/acerca_de_mi.html'

