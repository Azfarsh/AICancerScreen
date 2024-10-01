# cancer_detection/views.py
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')  # Render home.html

def about(request):
    return render(request, 'about.html')  # Render about.html

def services(request):
    return render(request, 'services.html')  # Render services.html

def contact(request):
    return render(request, 'contact.html')  # Render contact.html

def blog(request):
    return render(request, 'blog.html')  # Render blog.html

def whitepapers(request):
    return render(request, 'whitepapers.html')  # Render whitepapers.html

def webinars(request):
    return render(request, 'webinars.html')  # Render webinars.html

def faq(request):
    return render(request, 'faq.html')  # Render faq.html

def how_it_works(request):
    return render(request, 'how_it_works.html')  # Render how_it_works.html

def pricing(request):
    return render(request, 'pricing.html')  # Render pricing.html

def testimonials(request):
    return render(request, 'testimonials.html')  # Render testimonials.html

def dashboard(request):
    return render(request, 'dashboard.html')  # Render dashboard.html

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # Add your subscription logic here (e.g., save to database, send email)
        return redirect('home')  # Redirect to home after subscription
    return redirect('home')  # Redirect to home if not POST


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to the home page or dashboard
        else:
            messages.error(request, "Invalid email or password. Please try again.")
    
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose another one.')
            return redirect('register')

        # Create a new user
        user = User.objects.create_user(username=username, password=password)
        user.save()  # Save the user to the database

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')  # Redirect to login page after successful registration

    return render(request, 'register.html')
