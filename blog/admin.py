from django.contrib import admin
from .models import About, Contact, Footer,\
 Hero,Project, Tag, Technology, Testimonial


class AboutAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'icon')
  list_display_links = ('id', 'title')
  search_fields = ('title', 'icon')
  list_per_page = 20

admin.site.register(About, AboutAdmin)

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'address', 'email')
  list_display_links = ('id', 'email')
  search_fields = ('title', 'email')
  list_per_page = 20

admin.site.register(Contact, ContactAdmin)

admin.site.register(Footer)

admin.site.register(Hero)

class ProjectAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'tags')
  list_per_page = 20

admin.site.register(Project, ProjectAdmin)

admin.site.register(Tag)

class TechnologyAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'icon')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'icon')
  list_per_page = 20

admin.site.register(Technology, TechnologyAdmin)

class TestimonialAdmin(admin.ModelAdmin):
  list_display = ('id', 'author_name', 'author_title', 'author_photo')
  list_display_links = ('id', 'author_name')
  search_fields = ('author_name', 'author_title', 'author_photo')
  list_per_page = 20

admin.site.register(Testimonial, TestimonialAdmin)