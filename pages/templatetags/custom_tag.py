from django import template
import cv2
import numpy as np
import datetime
from django.utils import timezone


register = template.Library()


@register.simple_tag
def content_shortcut(content):
    if len(content) <= 100 :
        return content
    else:
        return content[:100]


@register.simple_tag
def detail_url(num):

    return "/kimverly/detail/"+str(num)

@register.filter(name='times')
def times(a,b):
    return range(a,b)

@register.filter
def get_recent_10(all_board):

    return all_board.order_by('-b_date')[:15]
@register.filter
def recent_order(all_board):

    return all_board.order_by('-b_date')

@register.inclusion_tag('pages/index.html', takes_context=True)
def render_carousel(context, carousel, carousel_id=None):
    carousel_id = carousel_id or 'carousel-%d' % carousel.pk
    context.update({
        'carousel': carousel,
        'carousel_id': carousel_id,
    })
    return context

@register.filter
def in_category(things, ids):
    return things.filter(f_id=ids)


