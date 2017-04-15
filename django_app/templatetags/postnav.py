from django import template

register = template.Library()

@register.inclusion_tag('post_detail.html')
def postnav(post, post_num):
    return {'post': post, 'post_num': post_num}
