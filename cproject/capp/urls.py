from django.urls import path
from . import views
app_name='shop'
urlpatterns = [

    path('',views.home,name='home'),
    path('ComputerScience',views.cs,name='ComputerScience'),
    path('BioMaths',views.bio,name='BioMaths'),
    path('Commerce',views.com,name='Commerce'),
    path('Humanities',views.hum,name='Humanities'),
    path('PhysicalEducation',views.pe,name='PhysicalEducation'),


]