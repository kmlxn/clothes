from django.db import models
from collections import namedtuple
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy as _pg
from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Clothing(models.Model):
    Choice = namedtuple("Choice", ["key", "caption", "url_name"])
    ChoicesContainer = namedtuple("ChoicesContainer",
        ["caption", "field_name", "url_name", "choices"])

    genders = ChoicesContainer(_("Gender/Age"), "gender", _pg("url", "gender"), (
        Choice(1, _("Men"), _pg("url", "men")),
        Choice(2, _("Women"), _pg("url", "women")),
        Choice(3, _("Unisex"), _pg("url", "unisex")),
        Choice(4, _("Boys"), _pg("url", "boys")),
        Choice(5, _("Girls"), _pg("url", "girls")),
        Choice(6, _("Kids unisex"), _pg("url", "kids_uni")),
    ))

    seasons = ChoicesContainer(_("Season"), "season", _pg("url", "season"), (
        Choice(1, _("Winter"), _pg("url", "winter")),
        Choice(2, _("Spring"), _pg("url", "spring")),
        Choice(3, _("Summer"), _pg("url", "summer")),
        Choice(4, _("Autumn"), _pg("url", "autumn")),
    ))

    filters = (seasons, genders)

    def get_choices(choices_container):
        return tuple((ch.key, ch.caption) for ch in choices_container.choices)

    @classmethod
    def filter(self, params):
        filtering_params = {}
        for filt_url_name, choice_url_name in params.items():
            filt = self.getFilterByUrlName(filt_url_name)
            choice_key = self.matchAndGetKey(filt.choices, choice_url_name)
            filtering_params[filt.field_name] = choice_key

        return self.objects.filter(**filtering_params)

    @classmethod
    def matchAndGetKey(self, choices, choice_url_name):
        for choice in choices:
            if choice.url_name == choice_url_name:
                return choice.key
        return None

    @classmethod
    def getFilterByUrlName(self, url_name):
        for filt in self.filters:
            if url_name == filt.url_name:
                return filt
        return None

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    photo = ThumbnailerImageField(upload_to='images', verbose_name=_("Photo"))
    gender = models.IntegerField(verbose_name=genders.url_name,
        choices=get_choices(genders))
    season = models.IntegerField(verbose_name=seasons.caption,
        choices=get_choices(seasons))
    category = models.ForeignKey(Category, verbose_name=_("Category"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Clothing")
        verbose_name_plural = _("Clothes")


class Option(models.Model):
    key = models.CharField(max_length=255, verbose_name=_("Key"))
    value = models.CharField(max_length=255, verbose_name=_("Value"), null=True)
