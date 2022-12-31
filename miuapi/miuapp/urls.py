from django.urls import path
from miuapp import views

urlpatterns = [
    path('miuapp/', views.api_list),
    path('apidetails/<int:pk>/', views.api_detail)

]