from django.urls import path
from .views import post_list, create_post #import the view function

urlpatterns = [
    path('', post_list, name='post_list'), #add the URL pattern
    path('new/', create_post, name='create_post'),
]