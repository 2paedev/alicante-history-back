from django.contrib import admin

from .models import CustomImage


@admin.register(CustomImage)
class CustomImageAdmin(admin.ModelAdmin):
    model = CustomImage
