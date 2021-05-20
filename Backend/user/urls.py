from django.urls import path

from . import views

urlpatterns = [
    path('<slug:id>/update/', views.Update, name='Update'),
    path('<slug:id>/delete/', views.Delete, name='Delete'),

]