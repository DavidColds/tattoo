from django.shortcuts import render

def home(request):
    return render(request, 'base/home.html')

def about(request):
    return render(request, 'base/about.html', {'title': 'About'})

def contact(request):
    return render(request, 'base/contact.html', {'title': 'Contact'})

def art(request):
    return render(request, 'base/art.html', {'title': 'Art'})

def portfolio(request):
    return render(request, 'base/portfolio.html', {'title': 'Portfolio'})