from django import template

register = template.Library()

@register.inclusion_tag('post_detail.html')
def postnav(post):
    return {'post': post}
