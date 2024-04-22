from django.contrib import admin
from django.db.models import Q
from django.contrib import messages
##################
from home.models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    search_fields = ['nome',]
    list_display = ('nome', 'classificacao', 'campus', 'modalidade', 'periodo')
    list_filter = ('classificacao', 'campus', 'modalidade', 'periodo')
    list_per_page = 10
