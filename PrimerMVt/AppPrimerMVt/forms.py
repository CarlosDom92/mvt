from datetime import date
from django import forms

class FamiliaresFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellidos = forms.CharField(max_length=60)
    fechaNacimiento  =  forms.DateField()

class ParentescoFormulario(forms.Form):
    parentesco = forms.CharField()