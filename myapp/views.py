#from django.shortcuts import render

# Create your views here.
#from django.http import HttpResponse

#def home(request):
  #return HttpResponse("Hello, world!")

# Importing necessary modules
# myapp/views.py
# myapp/views.py
from django.shortcuts import render
from django.conf import settings
from django.templatetags.static import static



def index(request):
    return render(request, 'myapp/index.html')
def image_gallery(request):
    # Example logic to list images from the static directory
    image_list = [
        'images/wp4469452-5120x3200-wallpapers.jpg',
        'images/wp4469453-5120x3200-wallpapers.jpg'
    ]
    
    # Add full URLs to the list
    image_list = [static(image_path) for image_path in image_list]

    return render(request, 'myapp/image_gallery.html', {'images': image_list})

