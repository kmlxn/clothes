from django.db import models
from collections import namedtuple
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy
from django.conf import settings
from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    url_name = models.CharField(max_length=255, verbose_name=_("Url Name"))


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Clothing(models.Model):
    Choice = namedtuple("Choice", ["key", "caption", "url_name"])
    FilterParameter = namedtuple("FilterParameter",
        ["caption", "field_name", "url_name", "choices"])

    genders = FilterParameter(
        _("Gender/Age"),
        "gender",
        pgettext_lazy("url", "gender"),
        (
            Choice(1, _("Men"), pgettext_lazy("url", "men")),
            Choice(2, _("Women"), pgettext_lazy("url", "women")),
            Choice(3, _("Unisex"), pgettext_lazy("url", "unisex")),
            Choice(4, _("Boys"), pgettext_lazy("url", "boys")),
            Choice(5, _("Girls"), pgettext_lazy("url", "girls")),
            Choice(6, _("Kids unisex"), pgettext_lazy("url", "kids_uni")),
        )
    )

    seasons = FilterParameter(
        _("Season"),
        "season",
        pgettext_lazy("url", "season"),
        (
            Choice(1, _("Winter"), pgettext_lazy("url", "winter")),
            Choice(2, _("Spring"), pgettext_lazy("url", "spring")),
            Choice(3, _("Summer"), pgettext_lazy("url", "summer")),
            Choice(4, _("Autumn"), pgettext_lazy("url", "autumn")),
        )
    )

    filter_parameters = (seasons, genders)


    def get_filter_param_choices(choices_container):
        return tuple((ch.key, ch.caption) for ch in choices_container.choices)


    @classmethod
    def filter(cls, params):
        filtering_params = {}

        for param_url_name, choice_url_name in params.items():
            param = cls.get_filter_param_by_url_name(param_url_name)
            choice_key = cls.get_choice_db_key(param, choice_url_name)
            filtering_params[param.field_name] = choice_key

        return cls.objects.filter(**filtering_params)


    @staticmethod
    def get_choice_db_key(filtering_param, choice_url_name):
        for choice in filtering_param.choices:
            if choice.url_name == choice_url_name:
                return choice.key
        return None


    @classmethod
    def get_filter_param_by_url_name(cls, url_name):
        for filt in cls.get_filter_params():
            if url_name == filt.url_name:
                return filt
        return None


    @classmethod
    def get_filter_params(cls):
        categories = Category.objects.all()
        choices = tuple(cls.Choice(x.pk, x.title, x.url_name) for x in categories)
        categories_filter_param = cls.FilterParameter(
            _("Category"),
            "category",
            pgettext_lazy("url", "category"),
            choices
        )
        return cls.filter_parameters + (categories_filter_param,)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = _("Clothing")
        verbose_name_plural = _("Clothes")


    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    photo = ThumbnailerImageField(upload_to='images', verbose_name=_("Photo"))
    gender = models.IntegerField(verbose_name=genders.url_name,
        choices=get_filter_param_choices(genders))
    season = models.IntegerField(verbose_name=seasons.caption,
        choices=get_filter_param_choices(seasons))
    category = models.ForeignKey(Category, verbose_name=_("Category"))


class Option(models.Model):
    key = models.CharField(max_length=255, verbose_name=_("Key"), unique=True)
    value = models.CharField(max_length=255, verbose_name=_("Value"), null=True)


    def __str__(self):
        return self.key


    class Meta:
        verbose_name = _("Option")
        verbose_name_plural = _("Options")


    @classmethod
    def get_dynamic_options(cls):
        options = {}
        for key in settings.DYNAMIC_OPTIONS:
            try:
                options[key] = cls.objects.get(key=key).value
            except cls.DoesNotExist:
                options[key] = None
        return options
