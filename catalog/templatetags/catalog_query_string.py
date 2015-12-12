from django import template

register = template.Library()


@register.tag
def query_string_set_value(parser, token):
    """
    Django template tag to set url query string parameter
    or replace parameter's value if it's already set

    ---------
    USAGE

    {% query_string_set_value 'tag_name_param' param_value %}

    ---------
    EXAMPLE (page_num is context variable):

    src="{% query_string_set_value 'page' page_num %}"

    ---------
    RESULT (if page_num = 3):

    (if query string was ?gender=male)
    src="?gender=male&page=3"

    (if query string was ?gender=male&page=2)
    src="?gender=male&page=3"

    (if there was no query string)
    src="?page=3"

    ---------
    REQUIRES to set this in settings.py:

    TEMPLATES = [{
        ...
        'OPTIONS': {
            ...
            'context_processors': [
                ...
                'django.core.context_processors.request',
                ...
            ],
            ...
        },
        ...
    }]
    """

    tag_name_param, tag_value_param = get_tag_params(token)

    return QueryStringSetValueNode(tag_name_param, tag_value_param)


def get_tag_params(token):
    try:
        tag_name, param_name, param_value_variable_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires 2 arguments" % token.contents.split()[0]
        )

    return param_name, param_value_variable_name


class QueryStringSetValueNode(template.Node):
    def __init__(self, tag_name_param, tag_value_param):
        self.tag_value_param = tag_value_param
        self.tag_name_param = tag_name_param


    def render(self, context):
        dict_ = context.request.GET.copy()
        query_string_param_name = self.get_value_of_tag_arg(context, self.tag_name_param)
        query_string_param_value = self.get_value_of_tag_arg(context, self.tag_value_param)

        if query_string_param_value == '':
            dict_.pop(query_string_param_name, None)
        else:
            dict_[query_string_param_name] = query_string_param_value

        return '?' + dict_.urlencode()


    def get_value_of_tag_arg(self, context, tag_argument):
        if self.represents_string(tag_argument):
            value = tag_argument[1:-1]
        else:
            value = self.get_variable_value_from_template_context(context, tag_argument)

        return value


    @staticmethod
    def represents_string(tag_argument):
        if tag_argument[0] == tag_argument[-1] and tag_argument[0] in ('"', "'"):
            return True
        return False


    @staticmethod
    def get_variable_value_from_template_context(context, variable_name):
        var = template.Variable(variable_name)

        return var.resolve(context)
