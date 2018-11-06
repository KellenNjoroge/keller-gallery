from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Category, Location


# Create your views here.
def index(request):
    images = Image.getImages()
    categories = Category.getcategories()
    return render(request, 'index.html', {'images': images, "categories": categories})


def singleimage(request, image_id):
    try:
        image = Image.objects.get(id=image_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "location.html", {"image": image})


def imagesbylocation(request, ):
    if 'images' in request.GET and request.GET["images"]:
        area = request.GET.get("images")
        searched_images = Image.collectimagelocation(area)
        message = f"{area}"

        return render(request, 'location.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'location.html', {"message": message})


def imagesbycategory(request, ):
    if 'images' in request.GET and request.GET["images"]:
        cat = request.GET.get("images")
        searched_images = Image.collectimagecategory(cat)
        message = f"{cat}"

        return render(request, 'category.html', {"message": message, "images": searched_images})

    else:
        message = "You haven't searched for any existing Category"
        return render(request, 'location.html', {"message": message})
