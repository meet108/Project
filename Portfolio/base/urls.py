from django.contrib import admin
from django.urls import path, include
from base import views

admin.site.site_header = 'Login to Developer Meet'
admin.site.site_title = 'Welcome to Meet''s Dashboard'
admin.site.index_title = 'Welcome to this portal'
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='project'),
    path('contact', views.contact, name='contact'),
]
