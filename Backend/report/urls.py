from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('log_reports/',views.login_reports,name='log In Users'),
    path('loggedin/',views.loggedin,name="Logged in users"),
    path('users/',views.users,name="Users list"),
]