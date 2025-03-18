# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create_procedimiento/', views.CreateProcedimiento.as_view(), name='create_procedimiento'),
    path('update_procedimiento/<int:pk>/', views.UpdateProcedimiento.as_view(), name='update_procedimiento'),
    path('list_procedimiento/', views.ListProcedimientos.as_view(), name='list_procedimiento'),
    path('details_procedimiento/<int:pk>/', views.DetailsProcedimiento.as_view(), name='details_procedimiento'),
]
