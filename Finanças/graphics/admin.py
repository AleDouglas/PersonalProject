from django.contrib import admin

# Register your models here.
from .models import Gain, Lose, Financa


@admin.register(Gain)
class GainPost(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'valor']
    exclude = ['usuario']

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        super().save_model(request, obj, form, change)

@admin.register(Lose)
class LosePost(admin.ModelAdmin):
    list_display = ['usuario', 'data', 'valor']
    exclude = ['usuario']

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        super().save_model(request, obj, form, change)

@admin.register(Financa)
class FinancaPost(admin.ModelAdmin):
    list_display = ['usuario', 'valor', 'credor']
    exclude = ['usuario']

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        super().save_model(request, obj, form, change)

