from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "climatechanges/index.html")


def about(request):
    return render(request, "climatechanges/about.html")

def contact(request):
    return render(request, "climatechanges/contact.html")

def login(request):
    return render(request, "climatechanges/login.html")

def signin(request):
    return render(request, "climatechanges/signin.html")
