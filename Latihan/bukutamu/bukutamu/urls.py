from django.contrib import admin
from django.urls import path
from daftar import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name="home"),
    path('daftar/', views.Daftar,name="daftar"),
    path('contact/', views.Contact,name="contact"),

]
