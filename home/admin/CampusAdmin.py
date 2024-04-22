from django.contrib import admin
from django.db.models import Q
from django.contrib import messages
##################
from home.models import Campus

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    search_fields = ['campus']

