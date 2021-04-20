"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import homepage_view, about_view, contact_view, my_works_view, portfolio_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # pages urls
    path('', homepage_view, name='home'),
    path('home/', homepage_view, name='home'),
    path('about/', about_view, name='about'),
    # path('my_works/', my_works_view, name='my_works'),
    path('portfolio/', portfolio_view, name='portfolio'),
    path('contact/', contact_view, name='contact'),

    # my_works_blog urls
    path('my_works/', include('my_works_blog.urls', namespace='my_works')),
]
