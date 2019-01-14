from django.urls import path
from . import views

urlpatterns = [
    path('<int:article_id>', views.blog_detail, name="article_detail"), # localhost:8000/blog/1
]