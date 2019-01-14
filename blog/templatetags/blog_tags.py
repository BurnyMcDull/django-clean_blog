from django import template
from ..models import Post, Category
from django.db.models.aggregates import Count
register = template.Library()

@register.simple_tag
def get_recent_posts():
    return Post.objects.all().order_by('-created_time')

@register.simple_tag
def get_archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories(id):
    post_list=Post.objects.filter(category_id=id).order_by('-created_time') 
    print(id)
    print(post_list)
    return post_list