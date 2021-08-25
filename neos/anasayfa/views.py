import kategori
from kategori.models import kategoriler
from django.shortcuts import render,HttpResponse
from kategori.models import urunl
# Create your views here.
def anasayfa(request):
    kategori = kategoriler.objects.all()
    sliderdata = urunl.objects.all()[:3]
    context ={ "sliderdata": sliderdata ,"kategori" : kategori }
    return render(request,"index.html",context)

def ank(request):
    kategori = kategoriler.objects.all()
    sliderdata = urunl.objects.all()[:3]
    context ={ "sliderdata": sliderdata ,"kategori" : kategori }
    return render(request,"anktod.html" ,context)

def ilet(request):
    kategori = kategoriler.objects.all()
    sliderdata = urunl.objects.all()[:3]
    context ={ "sliderdata": sliderdata ,"kategori" : kategori }
    return render(request,"iletisim.html" ,context)

