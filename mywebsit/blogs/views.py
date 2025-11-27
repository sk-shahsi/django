import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,Http404
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.loader import render_to_string

# Create your views here.

blog_details = [

    {
        "slug": "python-intro",
        "image": "Python_image.jpg",
        "date": datetime.date(2025, 11, 22),
        "title": "Python  Introduction",
        "preview": """
        Python is an open-source high leval programing language that is used eidely,
        Application of python are software development, data science, AI & ML, etc....
        """,
        "content": """ Python is a high-level , multi-paradigm, and general-purpose programing language,
        python provides a rich frameworks, tools, and libraries that allow you to build an application
        """,
    },
    {
"slug": "django-basic",
        "image": "Python_image.jpg",
        "date": datetime.date(2025, 11, 22),
        "title": "Python  Introduction",
        "preview": """
        Python is an open-source high leval programing language that is used eidely,
        Application of python are software development, data science, AI & ML, etc....
        """,
        "content": """ Python is a high-level , multi-paradigm, and general-purpose programing language,
        python provides a rich frameworks, tools, and libraries that allow you to build an application
        """,
    },
    {"slug": "python-oops",
        "image": "Python_image.jpg",
        "date": datetime.date(2025, 11, 22),
        "title": "Python  Introduction",
        "preview": """
        Python is an open-source high leval programing language that is used eidely,
        Application of python are software development, data science, AI & ML, etc....
        """,
        "content": """ Python is a high-level , multi-paradigm, and general-purpose programing language,
        python provides a rich frameworks, tools, and libraries that allow you to build an application
        """,},
    {"slug": "regex",
        "image": "Python_image.jpg",
        "date": datetime.date(2025, 11, 22),
        "title": "Python  Introduction",
        "preview": """
        Python is an open-source high leval programing language that is used eidely,
        Application of python are software development, data science, AI & ML, etc....
        """,
        "content": """ Python is a high-level , multi-paradigm, and general-purpose programing language,
        python provides a rich frameworks, tools, and libraries that allow you to build an application
        """,}


]

# def home_page(request):
#     return render(request, "blogs/index.html")
#     res_data = render_to_string("blogs/index.html")
#     # return HttpResponse(res_data)

def home_page(request):
   sort_blog=sorted(blog_details, key=lambda post: post["date"],reverse = True)
   latest_blog = sort_blog[:2]
   return render(request,'blogs/home.html',{'l_blogs':latest_blog})
    # # return render(request, "blogs/index.html")
    # res_data = render_to_string("blogs/index.html")
    # # return HttpResponse(res_data)



def blogpost(request):
    list_items =""
    # blog_list = list(blog_name.keys())
    return render(request, "blogs/allposts.html",{"blog_list":blog_details})
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
        # 2 raise Http404() #to production level
         res_data= render_to_string("404.html")
         return HttpResponseNotFound(res_data)
    # else :
    #     return HttpResponse(res)

# def blog_post_by_number(request,blog):
#    return HttpResponse(blog)


