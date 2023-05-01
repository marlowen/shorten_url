from django.contrib import admin
from .models import Listurls

@admin.register(Listurls)
class ListurlsAdmin(admin.ModelAdmin):
    list_display = ["fecha", "urloriginal", "urlcorto"]
