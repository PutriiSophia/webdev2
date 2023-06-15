from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from daftar.models import pdaftar
def Home(req):
    registrasi = pdaftar.objects.all ()
    return render(req,"landing.html")
def Daftar(req):
    registrasi = pdaftar.objects.all ()
    return render(req,"daftar.html",{"registrasi":registrasi})
def Contact(req):
    registrasi = pdaftar.objects.all ()
    return render(req,"contact.html",{"registrasi":registrasi})
