from django.contrib import admin
from django.db.models import Q
from django.contrib import messages
##################
from home.models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    search_fields = ['nome', 'cpf']
    list_display = ('nome', 'matricula', 'curso', 'formaDeIngresso' )
    list_filter = ('formaDeIngresso',)
    fieldsets = (
        ('Dados Pessoais', {
            'fields': ('nome', 'cpf', 'dataDeNasc', 'sexo', 'raca', 'foto')
        }),
        ('Dados do Curso', {
            'fields': ('curso', 'situacao', 'formaDeIngresso')
        })
    )
    list_per_page = 10