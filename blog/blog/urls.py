from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from helloworld.views import HelloWorld, postView

router = routers.SimpleRouter()
router.register('post', postView, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloWorld.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += router.urls
