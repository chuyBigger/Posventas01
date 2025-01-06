from django import forms
from ventas.models import Cliente, Producto

class AddClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Código Cliente: ',
            'nombre': 'Nombre del Cliente: ',
            'telefono': 'Telefono (Contacto): ',
        }

class EditClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('codigo', 'nombre', 'telefono')
        labels = {
            'codigo': 'Código Cliente: ',
            'nombre': 'Nombre del Cliente: ',
            'telefono': 'Telefono (Contacto): ',
        }
        widgets = {
            'codigo':forms.TextInput(attrs={'type':'text', 'id': 'codigo_editar'}),
            'nombre':forms.TextInput(attrs={'id':'nombre_editar'}),
            'telefono':forms.TextInput(attrs={'id':'telefono_editar'}),

        }

class AddProductoForm (forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigo', 'descripcion', 'imagen', 'costo', 'precio', 'cantidad')
        labels = {
            'codigo': 'Código Cliente: ',
            'descripcion': 'Descripcion: ',
            'imagen': 'Imagen: ',
            'costo': 'Costo del Producto: $ ',
            'precio': 'Precio Publico: $ ',
            'cantidad':'Cantidad en Almacen: '
        }

                    