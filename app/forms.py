from django import forms
from .models import Proveedor




class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = [
            'id_proveedor',
            'nombre_proveedor',

        ]
        labels = {
            'id_proveedor': 'ID',
            'nombre_proveedor': 'Nombre',
        }
        widgets = {
            'id_proveedor': forms.NumberInput(attrs={'class':'form-control'}),
            'nombre_proveedor': forms.TextInput(attrs={'class':'form-control'}),
        }
