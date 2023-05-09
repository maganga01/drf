from django.urls import path
from .views import AboutListView, ContactListView, FooterListView,\
HeroListView, ProjectListView, TechnologyListView, TestimonialListView

urlpatterns = [
  path('about', AboutListView.as_view()),
  path('contact', ContactListView.as_view()),
   path('footer', FooterListView.as_view()),
   path('hero', HeroListView.as_view()),
   path('project', ProjectListView.as_view()),
   path('technology', TechnologyListView.as_view()),
   path('testimonial', TestimonialListView.as_view()),
]