from django.contrib import admin
from .models import (
    Carousel,
    # Cta,
    Slide,
    Form,
    Field,
    ParallaxRow,
    ColumnInfo,
)


class CarouselSlidesInline(admin.TabularInline):
    model = Slide
    fields = [
        'Image',
        'AltText',
        'Carousel',
    ]


class CarouselAdmin(admin.ModelAdmin):
    list_display = [
        'Name',
    ]
    list_display_links = [
        'Name',
    ]
    list_filter = [
        'Name',
    ]
    search_fields = [
        'Name',
    ]
    inlines = [
        CarouselSlidesInline,
    ]
    list_per_page = 25


admin.site.register(Carousel, CarouselAdmin)


class FormFieldsInline(admin.TabularInline):
    model = Field
    fields = [
        'Name',
        'Type',
        'Label',
    ]


class FormAdmin(admin.ModelAdmin):
    list_display = [
        'Name',
        'Method',
    ]
    list_display_links = [
        'Name',
        'Method',
    ]
    list_filter = [
        'Name',
        'Method',
    ]
    search_fields = [
        'Name',
        'Method',
    ]
    inlines = [
        FormFieldsInline,
    ]
    list_per_page = 25


admin.site.register(Form, FormAdmin)


class ColumnsInline(admin.TabularInline):
    model = ColumnInfo
    fields = [
        'Title',
        'Stat',
    ]


class ParallaxRowAdmin(admin.ModelAdmin):
    list_display = [
        'Title',
        'Image',
    ]
    list_display_links = [
        'Title',
        'Image',
    ]
    list_filter = [
        'Title',
        # 'Image',
    ]
    search_fields = [
        'Title',
        # 'Image',
    ]
    inlines = [
        ColumnsInline,
    ]
    list_per_page = 25


admin.site.register(ParallaxRow, ParallaxRowAdmin)