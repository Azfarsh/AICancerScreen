# cancer_detection/views.py

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
