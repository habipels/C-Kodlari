from django import http
from django.shortcuts import render ,HttpResponse
from kategori.models import urunl
# Create your views here.
from kategori.models import kategoriler

def detaylar(request):
    return HttpResponse("Selamlar detaylar")

def egitim_detay(request,id,link):
    kategori = kategoriler.objects.all()
    sliderdata = urunl.objects.all()[:3]
    sliderdata = urunl.objects.filter( id= id)
    context = {"sliderdata" : sliderdata ,"kategori" : kategori }
    return render(request,"detay.html",context)