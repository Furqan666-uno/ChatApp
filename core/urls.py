from django.urls import path
from django.contrib.auth import views as auth_views # it is used for making login, logout pages from urls.py itself
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name="core/login.html"), name='login'),
]
