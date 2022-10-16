from django.shortcuts import render
import photo_to_print.controllers as controllers

# Create your views here.


def show_images(request):
    pics_list = controllers.list_pics()
    return render(request, "list_pics.html", context={"pics_list": pics_list})