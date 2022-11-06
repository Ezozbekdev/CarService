from django.urls import path
from .views import MainView, AboutView, FurnituresView, TestimonialsView, ContextView

urlpatterns = [
    path('', MainView, name='main'),
    path('about/', AboutView, name='about'),
    path('fur/', FurnituresView, name='fur'),
    path('testimonial/', TestimonialsView, name='test'),
    path('contact/', ContextView, name='cont')
]