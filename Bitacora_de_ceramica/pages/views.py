from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Pieza


class ListaPiezas(ListView):
    model = Pieza
    template_name = 'pages/lista_piezas.html'
    context_object_name = 'piezas'


class DetallePieza(DetailView):
    model = Pieza
    template_name = 'pages/detalle_pieza.html'
    context_object_name = 'pieza'


class CrearPieza(LoginRequiredMixin, CreateView):
    model = Pieza
    template_name = 'pages/formulario_pieza.html'
    fields = ['titulo', 'descripcion', 'imagen', 'contenido']
    success_url = reverse_lazy('lista_piezas')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EditarPieza(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Pieza
    template_name = 'pages/formulario_pieza.html'
    fields = ['titulo', 'descripcion', 'imagen', 'contenido']
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


class AcercaDeMiView(TemplateView):
    template_name = 'pages/acerca_de_mi.html'

