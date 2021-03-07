from django.shortcuts import render


# Create your views here.
def homepage_view(request):
    return render(request, 'homepage.html', {})


def about_view(request):
    return render(request, 'about.html', {})
