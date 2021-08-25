"""neos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from detaylar.views import detaylar
from django.contrib import admin
from django.urls import path , include 
from anasayfa import views
import hakkimizda.views as k
from django.conf import settings
from django.conf.urls.static import static
from kategori import views as kat
from detaylar import views as egt
from hakkimizda import views as hak
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include("anasayfa.urls"),name="anasayfa"),
    path('hakkimizda/', include("hakkimizda.urls"),name="hakkimizda"), 
    path('egitimler/', include("kategori.urls"),name="egitim"),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('kategori/<int:id>/<slug:link>/', kat.kategori_egitim, name='kategori_egitim'),
    path('detay/<int:id>/<slug:link>', egt.egitim_detay, name='egitim_detay'),
    path('akreditaston/', views.ank ,name="AKREDİTASYON"),
    path('iletisim/', views.ilet ,name="iletisim"),
    path('sss/', hak.sss ,name="sss"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf import settings

