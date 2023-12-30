from django.contrib import admin

from .models import Task

# * Clase que permitira al Admin visualizar campos como solo de lectura
class TaskAdmin(admin.ModelAdmin):
    # * IMPORTANTE: Los campos deben llamarse igual que las propiedades del Modelo y ser un Tupla
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Task, TaskAdmin)