from django.contrib import admin
from property.models import Property


class Properties(admin.ModelAdmin):
    list_display = ('id', 'cod_property')


admin.site.register(Property, Properties)
