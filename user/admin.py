from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User
# Register your models here.
@admin.register(User)
class drugadmin(admin.ModelAdmin):
    list_display = ['full_name']
    list_filter = ['full_name', 'phone']
    search_fields = ['full_name', 'email']

#admin.site.register(Drug, drugadmin)