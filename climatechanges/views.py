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
#----- SignUp-----#
from django.shortcuts import render, redirect 
from django.contrib.auth.hashers import make_password # Correct 
from .models import Customer

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        password_confirm = request.POST.get('pwd_2')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip_code')

        # Basic validation
        if password != password_confirm:
            return render(request, 'signup.html', {'error': 'Passwords do not match'})

        if Customer.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already taken'})

        # Save customer securely with a hashed password
        Customer.objects.create(
            username=username,
            full_name=full_name,
            email=email,
            password=make_password(password), 
            address=address,
            city=city,
            state=state,
            country=country,
            zip_code=zip_code
        )
        return redirect('login') # Redirect to your login page URL name

    return render(request, 'climatechanges/signup.html')