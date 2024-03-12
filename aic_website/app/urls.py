from django.urls import path
from app import views
urlpatterns = [
    path('',views.index_web, name='index_web'),
    path('about',views.about, name='about'),
    path('gallery',views.gallery, name='gallery'),
    path('blog',views.blog, name='blog'),
    path('partnership',views.partnership, name='partnership'),
    path('partnership_form/', views.partnership_form, name='partnership_form'),
    path('projects',views.projects, name='projects'),
    path('contact',views.contact, name='contact'),
    path('contact_form/', views.contact_form, name='contact_form'),  
]