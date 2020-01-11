from django.contrib import admin

from .models import Bibliography


@admin.register(Bibliography)
class BibliographyAdmin(admin.ModelAdmin):
    model = Bibliography
