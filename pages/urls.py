from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
import os
app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:b_type>/<int:id>/', views.detail, name='detail'),
    path('<slug:b_type>/', views.menu, name='menu'),
    #path('<slug:b_type>/write', views.write, name='write'),

]