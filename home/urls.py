from django.urls import path
from .views import index, login_handle, home, log_out

urlpatterns = [
    path('', index, name='login-form'),
    path('login/', login_handle, name="login"),
    path('home/', home, name="home"),
    path('logout/', log_out, name='logout'),
    
]
