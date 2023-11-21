from django.urls import path
from . import views
app_name='credentials'
urlpatterns = [


    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('order', views.order, name='order'),
    path('success', views.success, name='success'),
]