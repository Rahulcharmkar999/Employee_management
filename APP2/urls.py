from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name='display'),
    path('add/', views.addEmpData, name='add_employee'),
    path('update/<int:id>/', views.updateEmpData, name='update_employee'),
    path('delete/<int:id>/', views.deleteEmpData, name='delete_employee'),
]