from modeltranslation.translator import translator, TranslationOptions
from catalog.models import Clothing, Category, Option


class ClothingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'url_name')


class OptionTranslationOptions(TranslationOptions):
    fields = ('value',)


translator.register(Clothing, ClothingTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Option, OptionTranslationOptions)
