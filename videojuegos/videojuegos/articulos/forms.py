from dataclasses import fields
from django import forms
from articulos.models import Articulos, Categoria


class FromArticulo(forms.ModelForm):
    
    class Meta:
        model = Articulos
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'decripcion': forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'stock': forms.NumberInput(attrs={'class':'form-control'}),
            'genero': forms.Select(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),          
        }

class FromCategoria(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'
        
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'decripcion': forms.Textarea(attrs={'class':'form-control', 'rows':5}),         
        }