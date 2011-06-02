# coding: utf8
from django.template import Library, Node, TemplateSyntaxError
from apps.actions.helpers import get_content_type_or_None

register = Library()

class GetActionListNode(Node):
    def __init__(self, app_n_model, varname, *args, **kwargs):
        self.app_n_model = app_n_model
        self.varname = varname
    
    def render(self, context):
        user = context['user']
        ct = get_content_type_or_None(self.app_n_model[1:-1])
        if ct:
            model_class = ct.model_class()
            _actions = []
            ret = '<option value="None">-----</option>'
            for x in range(0, len(model_class.actions)):
                if hasattr(model_class.actions[x], 'has_perms'):
                    if user.has_perms(model_class.actions[x].has_perms):
                        ret += u'\n<option value="%s">%s</option>' % (x,
                            model_class.actions[x].short_description)
                else:
                    ret += u'\n<option value="%s">%s</option>' % (x,
                        model_class.actions[x].short_description)
            context[self.varname] = "<select name='action' id='id_action'>\n%s\n</select>" % ret
            return ''
            
        else:
            context[self.varname] = None
            return ''

#get_action_list for 'app.model' as varname
@register.tag
def get_action_list(parser, token):
    bits = token.contents.split()
    if len(bits) != 7:
        raise TemplateSyntaxError, "USE: {% get_action_list for 'app.model' as varname %}"
    if bits[1] != 'for' or bits[3] != 'as' or bits[5] != 'with':
        raise TemplateSyntaxError, "USE {% get_action_list for 'app.model' as varname %}" 
    return GetActionListNode(bits[2], bits[4])

