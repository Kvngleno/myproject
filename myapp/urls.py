# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),          # Home page URL
    path('gallery/', views.image_gallery, name='image_gallery'),  # Gallery page URL
]


