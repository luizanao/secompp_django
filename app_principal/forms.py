# -*- coding: utf-8 -*-

"""
Forms
--------------------------------------------------
Dsc:
--------------------------------------------------
"""

## Default
from django import forms

## Models
from app_principal.models import MaterialApoio


class MaterialApoioForm(forms.ModelForm):
	class Meta:
		model = MaterialApoio

class ContatoForm(forms.Form):
    assunto = forms.CharField(max_length=100)
    mensagem = forms.CharField()
    remetente = forms.EmailField()