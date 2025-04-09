from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import Stadium, StadiumImage


class StadiumImageAdmin(TabularInline):
    model = StadiumImage
    extra = 2

@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'manager', 'location', ]
    inlines = [StadiumImageAdmin, ]


