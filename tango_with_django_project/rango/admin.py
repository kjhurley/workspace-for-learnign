from django.contrib import admin
import rango.models
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display=('title','category','url')
    search_fields=['title']


admin.site.register(rango.models.Category)
admin.site.register(rango.models.Page, PageAdmin)
