from modeltranslation.translator import translator, TranslationOptions
from . import models


class ClothingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'url_name')


class OptionTranslationOptions(TranslationOptions):
    fields = ('value', 'comment')


class OrderTranslationOptions(TranslationOptions):
    pass


translator.register(models.Clothing, ClothingTranslationOptions)
translator.register(models.Category, CategoryTranslationOptions)
translator.register(models.Option, OptionTranslationOptions)
translator.register(models.Order, OrderTranslationOptions)
