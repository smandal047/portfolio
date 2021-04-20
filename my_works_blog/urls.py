from django.urls import path
from .views import my_works, my_works_detail, my_post_detail

app_name = 'my_works_blog'

urlpatterns = [
    path('', my_works, name='index'),
    path("<int:pk>/", my_works_detail, name='project_detail'),
    path("<int:pk>/<int:pk1>", my_post_detail, name='post_detail'),
]
