from django.conf import settings


def available_languages(request):
    langs = [(make_lang_url(code), lang) for code, lang in settings.LANGUAGES]

    return {"available_languages": langs}


def make_lang_url(code):
    return "/" if code == settings.MAIN_LANGUAGE else "/" + code + "/"
