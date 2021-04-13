from django.urls import path
from .views import my_works

app_name = 'my_works_blog'

urlpatterns = [
    path('', my_works, name='index'),
]
