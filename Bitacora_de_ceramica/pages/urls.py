from django.urls import path
from .views import (
    ListaPiezas,
    DetallePieza,
    CrearPieza,
    EditarPieza,
    BorrarPieza,
    AcercaDeMiView,
)

urlpatterns = [
    path('', ListaPiezas.as_view(), name='lista_piezas'),
    path('pieza/<int:pk>/', DetallePieza.as_view(), name='detalle_pieza'),
    path('crear/', CrearPieza.as_view(), name='crear_pieza'),
    path('<int:pk>/editar/', EditarPieza.as_view(), name='editar_pieza'),
    path('<int:pk>/borrar/', BorrarPieza.as_view(), name='borrar_pieza'),
    path('acerca-de-mi/', AcercaDeMiView.as_view(), name='acerca_de_mi'),
    
    
]

