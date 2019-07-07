from django import template
register = template.Library()

@register.filter('teamnum_to_key')
def teamnum_to_key(teamnum):
    return "frc{}".format(teamnum)
