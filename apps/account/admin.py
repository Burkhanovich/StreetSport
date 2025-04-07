from django.contrib import admin
from .models import Account

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'role')
    fields = ('name', 'phone_number', 'role')
    search_fields = ('id', 'name', 'phone_number', 'role' )
