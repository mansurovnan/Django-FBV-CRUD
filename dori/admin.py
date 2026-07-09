from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Drug
# Register your models here.
@admin.register(Drug)
class drugadmin(admin.ModelAdmin):
    list_display = ['name', 'fabric', 'price']
    list_filter = ['name']
    search_fields = ['title', 'desc']

#admin.site.register(Drug, drugadmin)pyho