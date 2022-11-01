from django.contrib import admin
from.models import Panel_Cliente


class Panel_Cliente_Admin(admin.ModelAdmin):
    readonly_fields = ("creado", ) # CAMPOS DE SOLO LECTURA 

# Register your models here.

admin.site.register(Panel_Cliente, Panel_Cliente_Admin)
