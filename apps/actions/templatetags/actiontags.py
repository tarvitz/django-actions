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
            for x in range(0, len(model_class.actions)):
                if hasattr(model_class.actions[x], 'has_perms'):
                    if user.has_perms(model_class.actions[x].has_perms):
                        _actions.append((x,
                            model_class.actions[x].short_description))
                else:
                    _actions.append((x, model_class.actions[x].short_description))
            context[self.varname] = _actions
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

@register.inclusion_tag('actions_select.html')
def show_actions(actions):
    return {'actions': actions}
