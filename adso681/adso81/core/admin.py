from django.contrib import admin
from .models import Novedades, Inventory, Incapacidad, Inscription, Activity, Donation

@admin.register(Novedades)
class NovedadesAdmin(admin.ModelAdmin):
    list_display = ('date', 'tipe_novedad',)
    list_display_links =('tipe_novedad',)
    search_fields =('tipe_novedad',)
    list_filter =('date',)
    list_per_page = 3
@admin.register(Inventory)
class InvetAdmin(admin.ModelAdmin):
    list_display =('date_register', 'quantity', 'description')
    list_editable =('quantity',)
    list_per_page = 2
@admin.register(Donation)
class DonatAdmin(admin.ModelAdmin):
    list_display = ('date_donation', 'quantity','tipe_donation',)
    list_per_page = 3
@admin.register(Incapacidad)
class IncapAdmin(admin.ModelAdmin):
    list_display = ('date_inability', 'tipe_inability',)
    list_per_page = 3
@admin.register(Inscription)
class InscripAdmin(admin.ModelAdmin):
    list_display = ('number_id','name', 'last_name',)
    list_per_page = 5
@admin.register(Activity)
class ActivAdmin(admin.ModelAdmin):
    list_display = ('name_teacher', 'date_activity', 'name_activity',)
    list_per_page = 4
    search_fields = ('name_teacher',)