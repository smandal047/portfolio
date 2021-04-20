from django.shortcuts import render


# Create your views here.

# homepage
def homepage_view(request):
    return render(request, 'homepage.html', {})


# about page
def about_view(request):
    return render(request, 'about.html', {})


# myWorks page
def my_works_view(request):
    return render(request, 'my_works.html', {})



# myRhythm page
def portfolio_view(request):
    return render(request, 'portfolio.html', {})



# contact page
def contact_view(request):
    return render(request, 'contact.html', {})
