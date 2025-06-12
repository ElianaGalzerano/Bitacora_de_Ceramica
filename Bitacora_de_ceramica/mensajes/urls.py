from django.urls import path
from .views import inbox_view, enviar_mensaje_view, enviar_mensaje_a_view
from .views import borrar_mensaje_view

urlpatterns = [
    path('', inbox_view, name='inbox'),
    path('enviar/', enviar_mensaje_view, name='enviar_mensaje'),
    path('enviar/<str:username>/', enviar_mensaje_a_view, name='enviar_mensaje_a'),
    path('mensaje/<int:pk>/borrar/', borrar_mensaje_view, name='borrar_mensaje'),
]

