from django.contrib import admin
from ventas.models import Cliente, Producto

class Cliente_admin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'codigo')
    search_fields = ['nombre']
    readonly_fields = ('created', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register( Cliente, Cliente_admin)


class Producto_admin(admin.ModelAdmin):
    list_display = ('descripcion','cantidad', 'costo', 'imagen')
    search_fields = ['descripcion']
    readonly_fields = ('created', 'update')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register( Producto, Producto_admin)


# Register your models here.