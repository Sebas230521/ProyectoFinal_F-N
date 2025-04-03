from django.urls import path
from .views import CreateEstanque, UpdateEstanque, ListEstanque, DetailsEstanque

urlpatterns = [
    path('create_estanque/', CreateEstanque.as_view(), name='create_estanque'),
    path('update_estanque/<int:pk>/', UpdateEstanque.as_view(), name='update_estanque'),
    path('list_estanque/', ListEstanque.as_view(), name='list_estanque'),
    path('details_estanque/<int:pk>/', DetailsEstanque.as_view(), name='details_estanque'),
]
