from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView, logout_then_login

urlpatterns = [
    url(r"^$", views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='portal/login.html'), name='login'),
    url(r'^logout/$', logout_then_login, name='logout'),
]