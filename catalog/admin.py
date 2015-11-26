from django.contrib import admin

from . import models



class ClothingAdmin(admin.ModelAdmin):
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



class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'description']})
    ]
    list_display = ('title',)



admin.site.register(models.Clothing, ClothingAdmin)
admin.site.register(models.Category, CategoryAdmin)
