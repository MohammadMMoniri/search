from django.contrib import admin
from .models import links
# Register your models here.
class linkadmin(admin.ModelAdmin):
    # fields = ['searched_word', 'link', 'date']
    list_display = ['searched_word', 'date', 'link']

admin.site.register(links, linkadmin)