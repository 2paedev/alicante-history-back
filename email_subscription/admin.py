from django.contrib import admin

from .models import EmailSubscription


@admin.register(EmailSubscription)
class EmailSubscriptionAdmin(admin.ModelAdmin):
    model = EmailSubscription
