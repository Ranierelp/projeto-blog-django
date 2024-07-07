
from django.urls import include, path
from blog.views import index

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
]
