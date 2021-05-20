from django.urls import path

from . import views

urlpatterns = [
    path('email/<slug:id>/', views.email, name='email'),
    path('phone/', views.phone, name='phone'),
]