from typing import ContextManager
from django import http
from django.shortcuts import render,HttpResponse
from kategori.models import urunl ,kategoriler
# Create your views here.
def kategori_sayfasi(request):
    sliderdata = urunl.objects.all()[:10]
    kategori = kategoriler.objects.all()
    context ={ "sliderdata": sliderdata ,"kategori" :kategori}
    return render(request,"egitimler.html",context) 

def kategori_egitim(request,id,link):
    kategori = kategoriler.objects.all()
    sliderdata = urunl.objects.filter( category_id= id)
    context = {"sliderdata" : sliderdata ,"kategori" :kategori}
    return render(request,"egitimler.html",context)

