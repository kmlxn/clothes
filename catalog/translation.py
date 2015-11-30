from modeltranslation.translator import translator, TranslationOptions
from catalog.models import Clothing, Category


class ClothingTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


translator.register(Clothing, ClothingTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
