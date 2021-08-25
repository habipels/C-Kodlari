from django.contrib import admin
import kategori.models as model

# Register your models here.

class kategoriy_admin(admin.ModelAdmin):
    
    list_display = ["isim","create_at"]
    list_filter = ["create_at"]
class urun_admin(admin.ModelAdmin):
    
    list_display = ["isim","category","egitmen","fiyat","Durum","egitim_gunleri","egitim_tarihi","egitim_bitis_tarihi"]
  
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'answer','ordernumber','status']
    list_filter = ['status']
admin.site.register(model.kategoriler,kategoriy_admin)
admin.site.register(model.urunl,urun_admin)
admin.site.register(model.egitmen)
admin.site.register(model.FAQ,FAQAdmin)