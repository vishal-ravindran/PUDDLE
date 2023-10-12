from django.urls import path
from core.forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views # importing views from django authetication and renaming to avoid name clash with views

app_name ='core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name ='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form = LoginForm), name ='login'),
]