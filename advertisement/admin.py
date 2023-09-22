from django.contrib import admin
from advertisement.models import Advertisement


class Advertisements(admin.ModelAdmin):
    list_display = ('id', 'property', 'platform_name')


admin.site.register(Advertisement, Advertisements)
