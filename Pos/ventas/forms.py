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
        fields = ('codigo', 'imagen','cantidad', 'descripcion', 'costo', 'precio' )
        labels = {

            'codigo': 'Código Barras: ',
            'imagen': 'Imagen: ',
            'descripcion': 'Descripcion: ',
            'cantidad':'Cantidad en Almacen: ',
            'costo': 'Costo del Producto: $ ',
            'precio': 'Precio Publico: $ ',
            
        }

                    