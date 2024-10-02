# cancer_detection/urls.py

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('blog/', views.blog, name='blog'),  # Blog page
    path('whitepapers/', views.whitepapers, name='whitepapers'),  # Whitepapers page
    path('webinars/', views.webinars, name='webinars'),  # Webinars page
    path('faq/', views.faq, name='faq'),  # FAQ page
    path('how-it-works/', views.how_it_works, name='how_it_works'),  # How It Works page
    path('pricing/', views.pricing, name='pricing'),  # Pricing page
    path('testimonials/', views.testimonials, name='testimonials'),  # Testimonials page
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard page
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    
    # Authentication URLs
    path('login/', views.login_view, name='login'),  # Login view
    path('logout/', views.logout_view, name='logout'),  # Logout view
    path('register/', views.register, name='register'),  # Registration view
   
    # Social Authentication URLs
    path('oauth/', include('social_django.urls', namespace='social')),
    path('login/google/', views.google_login, name='google_login'),
    path('login/success/', views.login_success, name='login_success'),
]