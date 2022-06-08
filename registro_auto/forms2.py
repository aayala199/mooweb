from secrets import choice
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from pkg_resources import require
from .models import unirmeRegistro

#create a unirme form


class unirmeForm(ModelForm):
    class Meta:
        model=unirmeRegistro
        fields=('marca', 'modelo', 'year', 'millas', 'locacion', 'nombre','email', 'telefono')
        labels={
            'marca': '',
            'modelo':'',
            'year':'',
            'millas':'',
            'locacion':'',
            'nombre':'',
            'email':'',
            'telefono':'',
        }
        kmchoices={
            ('0-15000', '0-15000 km'),
            ('15-50000', '15-50000 km'),
            ('50-100000', '50-100000 km'),
            ('100-150000', '100-150000 km'),
            ('+150000', '+150000 km'),
        }
        yearChoises=[tuple([x,x]) for x in range(2016,2024)]
        locacionChoises=[
            ('guayaquil', 'Guayaquil'),
            ('quito', 'Quito'),
            ('cuenca', 'Cuenca'),
        ]
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'marca'}),
            'modelo':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'modelo'}),
            #'year':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'year'}),
            'year':forms.Select(attrs={'class': 'form-control', 'placeholder': 'year'},choices=yearChoises),
            #'millas':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'km', 'km': '[1,5,10]'}),
            'millas':forms.Select(attrs={'class':'form-control', 'placeholder':'km'},choices=kmchoices),
            #'locacion':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ciudad'}),
            'locacion':forms.Select(attrs={'class': 'form-control', 'placeholder': 'ciudad'}, choices=locacionChoises),
            #'nombre'  :forms.Select(attrs={'class': 'form-control', 'placeholder': 'nombre'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'nombre completo'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'telefono':forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'telefono'}),
        }


