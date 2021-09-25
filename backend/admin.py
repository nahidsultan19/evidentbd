from django.contrib import admin
from .models import Evident


class EvidentAdmin(admin.ModelAdmin):
    list_display = ('input_values', 'start_datetime', 'end_datetime')


admin.site.register(Evident, EvidentAdmin)
