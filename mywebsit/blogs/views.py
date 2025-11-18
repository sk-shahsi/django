from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

blog_name = {
    "python-basic": "<h1>Python post<h1>",
    "django-basic": "Django post",
    "python-oops": "<h1>Python oops post<h1>",
    "regex": "<h1>Regular expiration in python<h1>"

}
def home_page(request):
    return render(request, "blogs/index.html")
    res_data = render_to_string("blogs/index.html")
    # return HttpResponse(res_data)
def blogpost(request):
    list_items =""
    blog_list = list(blog_name.keys())
    for b in blog_list:
        blog_path = reverse("blog_post", args=[b])
        list_items += f'<li><a href="{blog_path}">{b.capitalize()}</li>'

    # res_data = """
    # <ul>
    # <li><a href="allposts/python-basic">Python basic</a></li>
    # <li><a href="allposts/django-basic">Django basic</a></li>
    #
    # </ul>
    # """
    res_data = f"<ul>{list_items}</ul>"
    return HttpResponse(res_data)

def python_intro(request):
    return HttpResponse("<h1>Python Introduction !!<h1>")

def django_basic_intro(request):
    return HttpResponse("<h1>Django Basic Introduction !!<h1>")

def python_oops(request):
    return HttpResponse("<h1>Python Oops Introduction !!<h1>")

def blog_post(request,blog):
    try:

        res = blog_name[blog]
        # if blog == "python-basic":
        #     res = "<h1>Python post<h1>"
        # elif blog == "django-basic":
        #     res = "<h1>Django post<h1>"
        # elif blog == "python-oops":
        #     res = "<h1>Python post<h1>"
        # else:
    except Exception :


        return HttpResponseNotFound("<h1>Blog not found<h1>")
    else :
        return HttpResponse(res)

# def blog_post_by_number(request,blog):
#    return HttpResponse(blog)
