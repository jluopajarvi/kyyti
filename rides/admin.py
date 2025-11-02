from django.contrib import admin
from .models import Organizer, OrganizerUser, Customer


@admin.register(Organizer)
class OrganizerAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(OrganizerUser)
class OrganizerUserAdmin(admin.ModelAdmin):
    list_display = ['user', 'organizer', 'role', 'created_at']
    list_filter = ['role', 'organizer']
    search_fields = ['user__username', 'organizer__name']
    readonly_fields = ['created_at']


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'organizer', 'created_at']
    list_filter = ['organizer']
    search_fields = ['user__username', 'organizer__name', 'notes']
    readonly_fields = ['created_at']
