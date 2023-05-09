from rest_framework.generics import ListAPIView
from rest_framework import permissions

from .models import About, Contact, Footer, Hero, Project, Technology, Testimonial
from .serializers import AboutSerializer, ContactSerializer,\
 FooterSerializer, HeroSerializer,ProjectSerializer, TechnologySerializer,\
 TestimonialSerializer


class AboutListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = About.objects.all()
  serializer_class = AboutSerializer
  pagination_class = None

class ContactListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Contact.objects.all()
  serializer_class = ContactSerializer
  pagination_class = None

class FooterListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Footer.objects.all()
  serializer_class = FooterSerializer
  pagination_class = None


class HeroListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Hero.objects.all()
  serializer_class = HeroSerializer
  pagination_class = None

class ProjectListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Project.objects.all()
  serializer_class = ProjectSerializer
  pagination_class = None


class TechnologyListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Technology.objects.all()
  serializer_class = TechnologySerializer
  pagination_class = None


class TestimonialListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Testimonial.objects.all()
  serializer_class = TestimonialSerializer
  pagination_class = None