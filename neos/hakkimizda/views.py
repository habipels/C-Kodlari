from django.shortcuts import render,HttpResponse
from kategori.models import egitmen
from kategori.models import kategoriler
from kategori.models import FAQ
# Create your views here.
def hakkimizda(request):
    kategori = kategoriler.objects.all()
    sliderdata = egitmen.objects.all()
    context ={ "sliderdata": sliderdata ,"kategori" :kategori }
    return render(request,"hakkimizda.html",context)

def sss(request):
    kategori = kategoriler.objects.all()
    sfaq = FAQ.objects.all()
    sliderdata = egitmen.objects.all()
    context ={ "sliderdata": sliderdata ,"sfaq" :sfaq ,"kategori" :kategori }
    return render(request,"sss.html",context)


def page_not_found_view(request):

    return HttpResponse("Sayfa Bulunamadı")


    