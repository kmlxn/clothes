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


admin.site.register(models.Clothing, ClothingAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Option, OptionAdmin)
