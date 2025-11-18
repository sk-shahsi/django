from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path("",views.home_page),

    path('allposts',views.blogpost),
    # path("allposts/python_intro",views.python_intro),
    # path("allposts/django_intro",views.django_basic_intro),
    # path("allposts/python-oops",views.python_oops),
    # path("allposts/<int:blog>",views.blog_post_by_number),
    path("allposts/<slug:blog>",views.blog_post, name="blog_post")
]




