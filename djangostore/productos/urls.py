from django.urls import path

from djangostore import views

app_namr = 'products'

urlpatterns = [
    path('', views.index ,name='index')]