from pyexpat import model
from re import search
from django.contrib import admin

from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

#admin.site.register(Article)- admin sayfasında özelliştirme yapmadığımızda bu kullanılıyor 

@admin.register(Article)            #üst taraftaki kullanım yerine bunu kullanıyoruz özelleştirme yapacağımız zaman
class ArticleAdmin(admin.ModelAdmin):

    list_display = ["title","author","created_date"]    #hem başlık bilgisi hemde yazar bilgisi görünsün özelleştirmesi

    list_display_links = ["title","author","created_date"]  #liste içindekiler link şeklini alır

    search_fields = ["title"]    #title bilgisine göre arama özelliği ekleme

    list_filter = ["created_date"]   #created_date e göre filtreleme ekledik.istersek title yada content de ekleyebilirdik
    class Meta:
        model = Article
