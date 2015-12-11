from django import template

register = template.Library()


@register.tag
def query_string_set_value(parser, token):
    """
    example (page_num is context variable):

    {% query_string_set_value 'page' page_num %}

    requires settings.py:

    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.core.context_processors.request',
    )
    """
    param_name, param_value_variable_name = validate_and_get_tag_params(token)
    return QueryStringSetValueNode(param_name, param_value_variable_name)


def validate_and_get_tag_params(token):
    try:
        tag_name, param_name, param_value_variable_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError(
            "%r tag requires 2 arguments" % token.contents.split()[0]
        )
    if not (param_name[0] == param_name[-1] and param_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError(
            "%r tag's argument should be in quotes" % tag_name
        )
    return param_name[1:-1], param_value_variable_name


class QueryStringSetValueNode(template.Node):
    def __init__(self, param_name, param_value_variable_name):
        self.param_value_variable_name = param_value_variable_name
        self.param_name = param_name

    def render(self, context):
        dict_ = context.request.GET.copy()
        param_value = self.get_variable_value_by_name(
            context, self.param_value_variable_name
        )
        dict_[self.param_name] = param_value
        return '?' + dict_.urlencode()

    @staticmethod
    def get_variable_value_by_name(context, name):
        var = template.Variable(name)
        try:
            return var.resolve(context)
        except template.VariableDoesNotExist:
            return ''
