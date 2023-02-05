from django.contrib import admin
from .models import Contacts

# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", "surname", "age")}
    list_display = ("name", "surname", "age", "slug",)
    
admin.site.register(Contacts, ContactsAdmin)