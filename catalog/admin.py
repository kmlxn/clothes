from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from . import models


class ClothingAdmin(TranslationAdmin):
    fieldsets = [
        (None,
            {'fields':
                ['title', 'description', 'gender',
                'season', 'photo', 'category']
            }
        )
    ]
    list_display = ('title', 'category', 'gender', 'season')
    list_filter = ['category', 'gender', 'season']
    search_fields = ['title']


class CategoryAdmin(TranslationAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'description', 'url_name']})
    ]
    list_display = ('title',)


class OptionAdmin(TranslationAdmin):
    fieldsets = [
        (None, {'fields': ['key', 'value']})
    ]
    list_display = ('key',)


class OrderAdmin(TranslationAdmin):
    fieldsets = [
        (None, {'fields':
            ['client_name', 'client_company', 'order_text', 'client_email',
            'client_phone', 'time']
        })
    ]
    list_display = ('client_name', 'client_company', 'order_text', 'time',
        'client_email', 'client_phone')


admin.site.register(models.Clothing, ClothingAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Option, OptionAdmin)
admin.site.register(models.Order, OrderAdmin)
