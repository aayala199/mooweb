
from django import forms


yearChoises=[tuple([x,x]) for x in range(2016,2024)]
kmChoises=[
    ('0-15000', '0-15000 km'),
    ('15-50000', '15-50000 km'),
    ('50-100000', '50-100000 km'),
    ('100-150000', '100-150000 km'),
    ('+150000', '+150000 km'),
]
locacionChoises=[
    ('guayaquil', 'Guayaquil'),
    ('quito', 'Quito'),
    ('cuenca', 'Cuenca'),
]

class FormularioRegistroAuto(forms.Form):
    
    marca = forms.CharField(label="Marca", required=True)
    modelo = forms.CharField(label="Modelo", required=True)
    #year = forms.IntegerField(label="Year", required=True)
    year= forms.IntegerField(label="Year", required=True , widget=forms.Select(choices=yearChoises))
    #kilometraje=forms.IntegerField(label="km", required=True)
    kilometraje=forms.CharField(label="km", required=True, widget=forms.Select(choices=kmChoises))
    locacion = forms.CharField(label="Ciudad", required=True, widget=forms.Select(choices=locacionChoises))
    email= forms.EmailField(label="Email", required=True)

    
