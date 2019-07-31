from django.contrib import admin
from .models import (
    Client,
    SocialMedia,
    BusinessHours,
    Asset,
    Item,
)


class BusinessHoursInline(admin.TabularInline):
    model = BusinessHours
    fields = [
        'BusinessId',
        'Day',
        'Open',
        'Close',
    ]


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    fields = [
        'LinkId',
        'Link',
        'Type',
    ]


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'Name',
        'Type',
        'Telephone',
        'Email',
        'Website',
        'City',
        'State',
        'Zip',
    ]
    list_display_links = [
        'id',
        'Name',
    ]
    list_filter = [
        'Type',
        'Name',
        'Website',
        'City',
        'State',
        'Zip',
    ]
    search_fields = [
        'Name',
        'Website',
    ]
    inlines = [
        BusinessHoursInline,
        SocialMediaInline,
    ]
    list_per_page = 25


admin.site.register(Client, ClientAdmin)


class ItemInline(admin.TabularInline):
    model = Item
    fields = [
        'Name',
        'Description',
        'Image',
        'Published',
        'Category',
    ]


class AssetAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'Title',
        'Type',
        'Description',
        'Published',
    ]
    list_display_links = [
        'Title',
        'Type',
    ]
    list_filter = [
        'Type',
    ]
    list_editable = [
        'Published',
    ]
    search_fields = [
        'Type',
    ]
    inlines = [
        ItemInline,
    ]
    list_per_page = 25


admin.site.register(Asset, AssetAdmin)
