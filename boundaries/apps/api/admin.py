from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from boundaries.apps.api.models import BoundarySet, Boundary

class BoundarySetAdmin(admin.ModelAdmin):
    list_filter = ('authority', 'domain')

admin.site.register(BoundarySet, BoundarySetAdmin)

class BoundaryAdmin(OSMGeoAdmin):
    list_display = ('kind', 'name', 'external_id')
    list_display_links = ('name', 'external_id')
    list_filter = ('kind',)

admin.site.register(Boundary, BoundaryAdmin)