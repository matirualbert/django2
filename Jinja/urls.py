from django.urls import path
from Jinja import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('', views.about, name='my_about'),
    path('contact/', views.contact, name='my_contact'),
    path('gallery/', views.gallery, name='my_gallery')

]