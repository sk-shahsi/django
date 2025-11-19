from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

blog_name = {
    "python-basic": "Python Basic Intro",
    "django-basic": "Django basic post",
    "python-oops": "Python oops post",
    "regex": "Regular expiration in python"

}
# def home_page(request):
#     return render(request, "blogs/index.html")
#     res_data = render_to_string("blogs/index.html")
#     # return HttpResponse(res_data)

def home_page(request):
    return render(request, "blogs/index.html")
    res_data = render_to_string("blogs/index.html")
    # return HttpResponse(res_data)

def blogpost(request):
    list_items =""
    blog_list = list(blog_name.keys())
    return render(request, "blogs/allposts.html",{"blog_list":blog_list})
    # for b in blog_list:
    #     blog_path = reverse("blog_post", args=[b])
    #     list_items += f'<li><a href="{blog_path}">{b.capitalize()}</li>'

    # res_data = """
    # <ul>
    # <li><a href="allposts/python-basic">Python basic</a></li>
    # <li><a href="allposts/django-basic">Django basic</a></li>
    #
    # </ul>
    # """
    # res_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(res_data)

def python_intro(request):
    return HttpResponse("<h1>Python Introduction !!<h1>")

def django_basic_intro(request):
    return HttpResponse("<h1>Django Basic Introduction !!<h1>")

def python_oops(request):
    return HttpResponse("<h1>Python Oops Introduction !!<h1>")
def process_blog_name(blog):
    blog_list = blog.split("-")
    return " ".join(blog_list)
    #return " ".join(blog_list).title()

def blog_post(request,blog):
    try:

        res = blog_name[blog]
        return render(request, "blogs/post.html",{"blog_text":res
                                                  ,"blog_name":process_blog_name(blog)})

        # if blog == "python-basic":
        #     res = "<h1>Python post<h1>"
        # elif blog == "django-basic":
        #     res = "<h1>Django post<h1>"
        # elif blog == "python-oops":
        #     res = "<h1>Python post<h1>"
        # else:
    except Exception :
        return HttpResponseNotFound("<h1>Blog not found<h1>")
    # else :
    #     return HttpResponse(res)

# def blog_post_by_number(request,blog):
#    return HttpResponse(blog)
