from rest_framework import serializers
from .models import About, Contact, Footer,\
 Hero, Project, Tag, Technology, Testimonial


class AboutSerializer(serializers.ModelSerializer):
  class Meta:
    model = About
    fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Contact
    fields = '__all__'

class FooterSerializer(serializers.ModelSerializer):
  class Meta:
    model = Footer
    fields = '__all__'

class HeroSerializer(serializers.ModelSerializer):
  class Meta:
    model = Hero
    fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tag
    fields = ('name',)


class ProjectSerializer(serializers.ModelSerializer):
  tags = TagSerializer(many=True)

  class Meta:
    model = Project
    fields = ('name', 'description', 'link', 'image', 'tags')

class TechnologySerializer(serializers.ModelSerializer):
  class Meta:
    model = Technology
    fields = '__all__'


class TestimonialSerializer(serializers.ModelSerializer):
  class Meta:
    model = Testimonial
    fields = '__all__'