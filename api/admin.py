from django.contrib import admin
from .models import Payload

class PayloadAdmin(admin.ModelAdmin):
    list_display = ('method', 'path','get','post')
    search_fields = ('get','post')

admin.site.register(Payload, PayloadAdmin)