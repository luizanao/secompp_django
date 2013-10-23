#-*- coding: utf-8 -*-
from app_principal.models import *
from django.contrib import admin

# class PatrocinadorAdmin(admin.ModelAdmin):
#     list_display = ('nome', 'url')

admin.site.register(Professor)
admin.site.register(MaterialApoio)
admin.site.register(Aluno)
admin.site.register(Projeto)
admin.site.register(Aviso)
admin.site.register(Disciplina)

